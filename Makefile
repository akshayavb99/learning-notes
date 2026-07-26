.PHONY: build serve

build:
	python scripts/gen_widget.py
	python scripts/gen_knowledge_graph.py
	zensical build --clean

serve:
	python scripts/gen_widget.py
	python scripts/gen_knowledge_graph.py
	zensical serve

