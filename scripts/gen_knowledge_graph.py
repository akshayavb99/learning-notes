#!/usr/bin/env python3
"""Generate curated graph data, explicit links, and scalable mention backlinks."""
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse
from collections import deque
import json, re, sys
import yaml
ROOT=Path(__file__).resolve().parent.parent
DOCS=ROOT/'docs'; MANIFEST=DOCS/'indexes/ai-ml-interview-prep-graph.yaml'; OUTPUT=DOCS/'javascripts/knowledge-graph-data.js'; FENCE=re.compile(r'```.*?```|~~~.*?~~~',re.S); CODE=re.compile(r'`[^`]*`')
MD=re.compile(r'(?<!\!)\[([^\]]*)\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)'); WIKI=re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]')
def load_md(path):
 text=path.read_text(encoding='utf-8'); meta={}
 if text.startswith('---'):
  parts=text.split('---',2)
  if len(parts)==3: meta=yaml.safe_load(parts[1]) or {}; text=parts[2]
 return meta,text
def fail(message): print('knowledge graph: ERROR: '+message,file=sys.stderr); raise SystemExit(1)
def canonical(path):
 p=PurePosixPath(path); p=p.parent if p.name=='index.md' else p.with_suffix(''); return p.as_posix() if p.as_posix()!='.' else 'index'
def slugify(value): return re.sub(r'[^a-z0-9]+','-',value.lower()).strip('-') or 'planned-node'
def parse_grouped_manifest(text):
 entries=[]; current_category='Uncategorized'; current=None
 for raw in text.splitlines():
  line=raw.strip()
  if not line or line.startswith('#') or line=='files:': continue
  if line.startswith('- name:'):
   current={'path':None,'name':line.split(':',1)[1].strip().strip('"\''),'category':current_category,'status':None}; entries.append(current)
  elif line.startswith('- path:'):
   current={'path':line.split(':',1)[1].strip().strip('"\''),'name':None,'category':current_category,'status':None}; entries.append(current)
  elif line.startswith('category:') or line.startswith('- category:'):
   current_category=line.split(':',1)[1].strip().strip('"\'') or 'Uncategorized'
   if current is not None: current['category']=current_category
  elif line.startswith('name:') and current is not None: current['name']=line.split(':',1)[1].strip().strip('"\'')
  elif line.startswith('path:') and current is not None: current['path']=line.split(':',1)[1].strip().strip('"\'')
 return entries
def read_manifest():
 text=MANIFEST.read_text(encoding='utf-8')
 # The manifest may use Jinja-style {# ... #} blocks to disable entries.
 text=re.sub(r'\{#.*?#\}', '', text, flags=re.S)
 try:
  raw=yaml.safe_load(text) or {}; entries=raw.get('files',[]) if isinstance(raw,dict) else raw
 except yaml.YAMLError:
  entries=parse_grouped_manifest(text)
 if not isinstance(entries,list): fail("manifest 'files' must be a YAML list")
 out=[]
 valid_statuses={'To be started','In Progress','Complete'}
 for i,item in enumerate(entries,1):
  if isinstance(item,str): path,name,cat,status=item,None,'Uncategorized',None
  elif isinstance(item,dict): path,name,cat,status=item.get('path'),item.get('name'),item.get('category') or 'Uncategorized',item.get('status')
  else: fail(f'files[{i}] must be a path or object')
  if path is None and (not isinstance(name,str) or not name.strip()): fail(f'files[{i}] needs a path or a non-empty name')
  if name is not None and (not isinstance(name,str) or not name.strip()): fail(f'files[{i}].name must be a non-empty string')
  if status is not None and status not in valid_statuses: fail(f"files[{i}].status must be one of: {', '.join(valid_statuses)}")
  if path is None: out.append({'path':None,'name':name.strip(),'category':str(cat),'status':status}); continue
  fragment=None
  if '#' in path: path,fragment=path.split('#',1); fragment=fragment.strip() or None
  path=path.replace('\\','/').lstrip('/').rstrip('/')
  candidate=DOCS/Path(path)
  if candidate.is_file() and candidate.suffix.lower()=='.md':
   source=candidate.resolve()
  elif not Path(path).suffix and (DOCS/Path(path+'.md')).is_file():
   path=path+'.md'; source=(DOCS/Path(path)).resolve()
  elif candidate.is_dir() and (candidate/'index.md').is_file():
   path=path.rstrip('/')+'/index.md'; source=(DOCS/Path(path)).resolve()
  else:
   source=candidate.resolve()
  if not path.endswith('.md') or DOCS not in source.parents: fail('invalid docs-relative Markdown path: '+path)
  if not source.is_file(): fail('listed file does not exist: docs/'+path)
  out.append({'path':path,'name':name.strip() if isinstance(name,str) else None,'category':str(cat),'status':status,'anchor':fragment})
 return out
def normalize(value):
 value=value.casefold(); value=re.sub(r'[_\W]+',' ',value,flags=re.UNICODE); return ' '+re.sub(r'\s+',' ',value).strip()+' '
def resolve(source,target,aliases):
 p=urlparse(target.strip())
 if p.scheme or p.netloc or p.path.startswith(('/','#')): return None
 value=PurePosixPath(PurePosixPath(source).parent,unquote(p.path)).as_posix().rstrip('/')
 candidates=[value]
 if not value.endswith('.md'): candidates.append(value+'.md')
 candidates.append(value+'/index.md')
 return next((aliases[x] for x in candidates if x in aliases),None)
def explicit_links(source,text,aliases):
 body=CODE.sub('',FENCE.sub('',text)); result=[]; seen=set()
 for match in list(MD.finditer(body))+list(WIKI.finditer(body)):
  if match.re is MD: label,target=match.group(1).strip(),match.group(2) or match.group(3)
  else: target,label=match.group(1).strip(),(match.group(2) or match.group(1)).strip()
  ident=resolve(source,target,aliases)
  if ident and (ident,label) not in seen: result.append({'target':ident,'label':label}); seen.add((ident,label))
 return result
def mention_matches(text, patterns):
 clean=CODE.sub('',FENCE.sub('',text)); normalized=normalize(clean); found={}
 for phrase,ident,title in patterns: found[ident]=found.get(ident,0)+normalized.count(phrase)
 return found
def build_matcher(nodes):
 trie=[{'next':{},'fail':0,'out':[]}]
 for ident,title in nodes:
  phrase=normalize(title)
  if phrase.strip()=='': continue
  state=0
  for char in phrase:
   next_state=trie[state]['next'].get(char)
   if next_state is None:
    next_state=len(trie); trie[state]['next'][char]=next_state; trie.append({'next':{},'fail':0,'out':[]})
   state=next_state
  trie[state]['out'].append((ident,title))
 queue=deque()
 for child in trie[0]['next'].values(): queue.append(child)
 while queue:
  state=queue.popleft()
  for char,child in trie[state]['next'].items():
   queue.append(child); fail=trie[state]['fail']
   while fail and char not in trie[fail]['next']: fail=trie[fail]['fail']
   trie[child]['fail']=trie[fail]['next'].get(char,0); trie[child]['out']+=trie[trie[child]['fail']]['out']
 return trie
def mention_matches(text,matcher):
 clean=CODE.sub('',FENCE.sub('',text)); normalized=normalize(clean); found={}; state=0
 for char in normalized:
  while state and char not in matcher[state]['next']: state=matcher[state]['fail']
  state=matcher[state]['next'].get(char,0)
  for ident,title in matcher[state]['out']: found[ident]=found.get(ident,0)+1
 return found
def main():
 raw_entries=read_manifest(); entries=[]; seen_planned=set()
 for item in raw_entries:
  if item['path'] is None:
   key=normalize(item['name'])
   if key in seen_planned:
    print('knowledge graph: warning: duplicate planned topic skipped: '+item['name'])
    continue
   seen_planned.add(key)
  entries.append(item)
 aliases={}; used=set()
 for item in entries:
  if item['path']:
   ident=canonical(item['path']); anchor=item.get('anchor')
   if anchor: ident=ident+'#'+anchor
   aliases.setdefault(item['path'],ident); aliases.setdefault(item['path'][:-3],ident)
   if item['path'].endswith('/index.md'): aliases.setdefault(item['path'][:-8],ident)
 nodes=[]; node_by_source={}
 for item in entries:
  path=item['path']
  if path:
   source=DOCS/Path(path); ident=canonical(path); anchor=item.get('anchor')
   if anchor: ident=ident+'#'+anchor
   meta,content=load_md(source); inferred=meta.get('title') or (source.parent.name if source.name=='index.md' else source.stem); title=item['name'] or (str(inferred) if meta.get('title') else re.sub(r'[-_]+',' ',str(inferred)).strip().title()); status=item.get('status') or 'Complete'; status_class={'To be started':'planned','In Progress':'in-progress','Complete':'complete'}[status]; url=None
   node_by_source[path]=ident
  else:
   title=item['name']; ident='planned/'+slugify(title); content=''; status=item.get('status') or 'To be started'; status_class={'To be started':'planned','In Progress':'in-progress','Complete':'complete'}[status]; url=None
  if ident in used: ident=ident+'#'+slugify(title)
  used.add(ident); nodes.append({'id':ident,'title':title,'status':status,'statusClass':status_class,'category':item['category'],'source':path,'anchor':item.get('anchor'),'url':url})
 node_titles=[(n['id'],n['title']) for n in nodes]; matcher=build_matcher(node_titles); node_by_id={n['id']:n for n in nodes}; edge_map={}
 for item in entries:
  path=item['path']
  if not path: continue
  source=DOCS/Path(path); source_id=node_by_source[path]; _,content=load_md(source)
  for link in explicit_links(path,content,aliases):
   if link['target']==source_id: continue
   key=(source_id,link['target']); edge=edge_map.setdefault(key,{'source':source_id,'target':link['target'],'label':node_by_id[link['target']]['title'],'kind':'explicit','count':0,'explicitCount':0,'mentionCount':0}); edge['explicitCount']+=1; edge['count']+=1; edge['label']=link['label'] or edge['label']
  for target,count in mention_matches(content,matcher).items():
   if target==source_id: continue
   key=(source_id,target); edge=edge_map.setdefault(key,{'source':source_id,'target':target,'label':node_by_id[target]['title'],'kind':'mention','count':0,'explicitCount':0,'mentionCount':0}); edge['mentionCount']+=count; edge['count']+=count; edge['kind']='explicit-and-mention' if edge['explicitCount'] else 'mention'
 edges=list(edge_map.values())
 OUTPUT.parent.mkdir(parents=True,exist_ok=True); OUTPUT.write_text('// Generated file.\nwindow.KNOWLEDGE_GRAPH = '+json.dumps({'nodes':nodes,'links':edges},ensure_ascii=False,indent=2)+';\n',encoding='utf-8'); print(f'knowledge graph: generated {len(nodes)} nodes and {len(edges)} links')
if __name__=='__main__': main()











