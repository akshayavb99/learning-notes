(function(){
  'use strict';
  var graphScript=document.currentScript;
  var vars=['--md-primary-fg-color','--md-accent-fg-color','--md-typeset-a-color','--md-primary-fg-color--light','--md-default-fg-color--light','--md-default-fg-color--lighter'];
  function theme(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim()||'#64748b'}
  function esc(s){return String(s).replace(/[&<>\"]/g,function(c){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c]})}
  function graphUrl(n){
    if(!n||!n.source)return null;
    var source=n.source.replace(/\\/g,'/').replace(/\.md$/i,'');
    if(source.endsWith('/index'))source=source.slice(0,-6);
    var root=window.__md_scope?new URL('.',window.__md_scope).href:null;
    if(!root){
      var script=graphScript||document.querySelector('script[src*="knowledge-graph.js"]');
      var scriptUrl=script?new URL(script.src,document.baseURI):null;
      root=scriptUrl?scriptUrl.href.replace(/javascripts\/knowledge-graph\.js(?:\?.*)?$/,''):new URL('/',location.href).href;
    }
    return new URL(source.replace(/^\/+/, '')+'/'+(n.anchor?'#'+n.anchor:''),root).href;
  }
  function init(root){
    if(root.dataset.kgReady)return; root.dataset.kgReady='1';
    var d=window.KNOWLEDGE_GRAPH||{nodes:[],links:[]}, svg=root.querySelector('[data-kg-svg]'), vp=root.querySelector('[data-kg-viewport]'), search=root.querySelector('[data-kg-search]'), select=root.querySelector('[data-kg-category]'), labels=root.querySelector('[data-kg-labels]'), details=root.querySelector('[data-kg-details]'), count=root.querySelector('[data-kg-count]'), empty=root.querySelector('[data-kg-empty]'), legend=root.querySelector('[data-kg-legend]');
    var by={},state={},selected='',hovered='',scale=1,tx=0,ty=0,drag=null,pan=null,layoutLocked=false,layoutSize='';
    d.nodes.forEach(function(n){by[n.id]=n;state[n.id]={x:0,y:0}});
    var cats=Array.from(new Set(d.nodes.map(function(n){return n.category||'Uncategorized'}))).sort(), colors={};
    cats.forEach(function(c,i){colors[c]=theme(vars[i%vars.length]);var o=document.createElement('option');o.value=c;o.textContent=c;select.appendChild(o)});
    legend.innerHTML='<div class="kg-legend-group"><strong class="kg-legend-title">Node categories</strong><div class="kg-legend-items">'+cats.map(function(c){return'<span class="kg-legend-item"><i class="kg-legend-swatch" style="background:'+colors[c]+'"></i>'+esc(c)+'</span>'}).join('')+'</div></div><div class="kg-legend-group"><strong class="kg-legend-title">Node status</strong><div class="kg-legend-items"><span class="kg-legend-item"><i class="kg-legend-swatch kg-legend-status-complete"></i>Complete</span><span class="kg-legend-item"><i class="kg-legend-swatch kg-legend-status-in-progress"></i>In Progress</span><span class="kg-legend-item"><i class="kg-legend-swatch kg-legend-status-planned"></i>To be started</span></div></div><div class="kg-legend-group"><strong class="kg-legend-title">Edges</strong><div class="kg-legend-items"><span class="kg-legend-item"><i class="kg-legend-edge"></i>Explicit link</span><span class="kg-legend-item"><i class="kg-legend-edge kg-legend-edge-mention"></i>Mention backlink</span><span class="kg-legend-item"><i class="kg-legend-edge kg-legend-edge-both"></i>Explicit + mention</span></div></div>';
    count.textContent=d.nodes.length+' notes Ãƒâ€šÃ‚Â· '+d.links.length+' links'; empty.hidden=!!d.nodes.length;
    var world=document.createElementNS('http://www.w3.org/2000/svg','g'),edgeLayer=document.createElementNS('http://www.w3.org/2000/svg','g'),nodeLayer=document.createElementNS('http://www.w3.org/2000/svg','g');
    svg.appendChild(world);world.append(edgeLayer,nodeLayer);var edgeEls=[],nodeEls={};
    d.links.forEach(function(l){if(!by[l.source]||!by[l.target])return;var e=document.createElementNS('http://www.w3.org/2000/svg','line');e.classList.add('kg-edge');e.classList.add('kg-edge-'+l.kind);edgeLayer.appendChild(e);edgeEls.push({d:l,e:e})});
    d.nodes.forEach(function(n){
      var g=document.createElementNS('http://www.w3.org/2000/svg','g'),c=document.createElementNS('http://www.w3.org/2000/svg','circle'),t=document.createElementNS('http://www.w3.org/2000/svg','text'),s=document.createElementNS('http://www.w3.org/2000/svg','text');
      c.classList.add('kg-node');c.setAttribute('r',8);c.setAttribute('fill',colors[n.category||'Uncategorized']);
      t.classList.add('kg-node-label');t.textContent=n.title;t.setAttribute('x',13);t.setAttribute('dy',4);
      s.classList.add('kg-node-status');s.textContent=n.status;s.setAttribute('x',13);s.setAttribute('y',22);
      g.setAttribute('role','button');g.setAttribute('tabindex','0');g.setAttribute('aria-label',n.title);g.setAttribute('aria-selected','false');g.append(c,t,s);nodeLayer.appendChild(g);nodeEls[n.id]={g:g,c:c,t:t,s:s,n:n};
      g.onclick=function(){selectNode(n)};g.onkeydown=function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();selectNode(n)}};g.onpointerenter=function(){hovered=n.id;render()};g.onpointerleave=function(){hovered='';render()};g.onpointerdown=function(e){e.stopPropagation();drag={id:n.id};g.setPointerCapture(e.pointerId)};
    });
    function selectNode(n){selected=n.id;detailsView();render()}
    function connected(a,b){return d.links.some(function(l){return(l.source===a&&l.target===b)||(l.target===a&&l.source===b)})}
    function visible(n){var q=search.value.toLowerCase();return(!q||n.title.toLowerCase().indexOf(q)>=0||n.status.toLowerCase().indexOf(q)>=0)&&(!select.value||(n.category||'Uncategorized')===select.value)}
    function detailsView(){
      if(!selected){details.innerHTML='<p class="kg-details-placeholder">Select a note to inspect its connections.</p>';return}
      var n=by[selected],href=graphUrl(n),ins=d.links.filter(function(l){return l.target===selected}),outs=d.links.filter(function(l){return l.source===selected}),open=href?'<a class="kg-detail-link" href="'+esc(href)+'">Open note ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢</a>':'<p class="kg-detail-status kg-detail-status-'+n.statusClass+'">'+esc(n.status)+'</p>';
      details.innerHTML='<p class="kg-detail-category" style="color:'+colors[n.category]+'">'+esc(n.category)+'</p><h2 class="kg-detail-title">'+esc(n.title)+'</h2>'+open+'<div class="kg-detail-stats"><div class="kg-detail-stat"><strong>'+outs.length+'</strong><span>outgoing</span></div><div class="kg-detail-stat"><strong>'+ins.length+'</strong><span>backlinks</span></div></div><h3>Connected notes</h3><ul class="kg-detail-list">'+ins.concat(outs).map(function(l){var o=by[l.source===selected?l.target:l.source];return'<li><a href="'+esc(graphUrl(o)||'#')+'">'+esc(o.title)+'</a></li>'}).join('')+'</ul>';
    }
    function seed(value){var h=2166136261;for(var i=0;i<value.length;i++){h^=value.charCodeAt(i);h=Math.imul(h,16777619)}return function(){h+=0x6D2B79F5;var t=h;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return((t^t>>>14)>>>0)/4294967296}}
    function layoutNodes(w,h){
      var key=Math.round(w)+'x'+Math.round(h);if(layoutLocked&&layoutSize)return;if(layoutSize===key)return;
      var random=seed(d.nodes.map(function(n){return n.id}).join('|')+'|'+key),left=90,right=180,top=70,bottom=80,minX=left,maxX=Math.max(left+1,w-right),minY=top,maxY=Math.max(top+1,h-bottom),positions={},links=[];
      d.nodes.forEach(function(n){positions[n.id]={x:minX+random()*(maxX-minX),y:minY+random()*(maxY-minY)}});
      d.links.forEach(function(l){if(by[l.source]&&by[l.target]&&l.source!==l.target)links.push(l)});
      for(var iteration=0;iteration<140;iteration++){
        var force={};d.nodes.forEach(function(n){force[n.id]={x:0,y:0}});
        for(var i=0;i<d.nodes.length;i++)for(var j=i+1;j<d.nodes.length;j++){
          var a=positions[d.nodes[i].id],b=positions[d.nodes[j].id],dx=a.x-b.x,dy=a.y-b.y,dist=Math.max(1,Math.sqrt(dx*dx+dy*dy)),push=9000/(dist*dist);
          force[d.nodes[i].id].x+=dx/dist*push;force[d.nodes[i].id].y+=dy/dist*push;force[d.nodes[j].id].x-=dx/dist*push;force[d.nodes[j].id].y-=dy/dist*push;
        }
        links.forEach(function(l){var a=positions[l.source],b=positions[l.target],dx=b.x-a.x,dy=b.y-a.y,dist=Math.max(1,Math.sqrt(dx*dx+dy*dy)),pull=(dist-105)*.018;force[l.source].x+=dx/dist*pull;force[l.source].y+=dy/dist*pull;force[l.target].x-=dx/dist*pull;force[l.target].y-=dy/dist*pull});
        d.nodes.forEach(function(n){var p=positions[n.id],f=force[n.id];f.x+=((minX+maxX)/2-p.x)*.002;f.y+=((minY+maxY)/2-p.y)*.002;p.x=Math.max(minX,Math.min(maxX,p.x+Math.max(-18,Math.min(18,f.x))));p.y=Math.max(minY,Math.min(maxY,p.y+Math.max(-18,Math.min(18,f.y))))});
      }
      d.nodes.forEach(function(n){state[n.id]=positions[n.id]});layoutSize=key;
    }
    function render(){
      var w=vp.clientWidth||800,h=vp.clientHeight||620;layoutNodes(w,h);svg.setAttribute('viewBox','0 0 '+w+' '+h);world.setAttribute('transform','translate('+tx+','+ty+') scale('+scale+')');
      d.nodes.forEach(function(n){var s=state[n.id],e=nodeEls[n.id];e.g.setAttribute('transform','translate('+s.x+','+s.y+')');e.g.setAttribute('aria-selected',selected===n.id?'true':'false');e.c.classList.toggle('kg-node-muted',!visible(n));e.c.classList.toggle('kg-node-active',selected===n.id);e.c.classList.toggle('kg-node-hover',hovered===n.id);e.c.classList.toggle('kg-node-hover-muted',!!hovered&&hovered!==n.id&&!connected(hovered,n.id));e.t.classList.toggle('kg-node-label-hover',hovered===n.id);e.s.classList.toggle('kg-node-status-complete',n.statusClass==='complete');e.s.classList.toggle('kg-node-status-planned',n.statusClass==='planned');e.s.classList.toggle('kg-node-status-in-progress',n.statusClass==='in-progress');e.t.style.display=labels.checked?'':'none';e.s.style.display=labels.checked?'':'none'});
      edgeEls.forEach(function(x){var a=state[x.d.source],b=state[x.d.target];x.e.setAttribute('x1',a.x);x.e.setAttribute('y1',a.y);x.e.setAttribute('x2',b.x);x.e.setAttribute('y2',b.y);var focus=selected||hovered;x.e.classList.toggle('kg-edge-active',!!focus&&(x.d.source===focus||x.d.target===focus));x.e.classList.toggle('kg-edge-hover',!!hovered&&(x.d.source===hovered||x.d.target===hovered));x.e.style.opacity=!hovered||x.d.source===hovered||x.d.target===hovered?'':'.12'});
    }
    function point(e){var r=svg.getBoundingClientRect();return{x:(e.clientX-r.left-tx)/scale,y:(e.clientY-r.top-ty)/scale}}
    svg.onpointermove=function(e){if(drag){layoutLocked=true;var p=point(e);state[drag.id].x=p.x;state[drag.id].y=p.y;render()}else if(pan){tx=pan.tx+e.clientX-pan.x;ty=pan.ty+e.clientY-pan.y;render()}};svg.onpointerup=function(){drag=pan=null};svg.onpointerdown=function(e){pan={x:e.clientX,y:e.clientY,tx:tx,ty:ty}};svg.onwheel=function(e){e.preventDefault();scale=Math.max(.35,Math.min(3,scale*(e.deltaY<0?1.1:.9)));render()};search.oninput=select.onchange=labels.onchange=render;root.querySelector('[data-kg-reset]').onclick=function(){scale=1;tx=ty=0;render()};detailsView();render();
  }
  function initAll(){document.querySelectorAll('[data-knowledge-graph]').forEach(init)}
  function start(){if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initAll,{once:true});else initAll();if(window.document$&&document$.subscribe)document$.subscribe(initAll)}
  start()
})();












