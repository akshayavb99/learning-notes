.PHONY: build serve

build:
	python scripts/gen_widget.py
	zensical build --clean

serve:
	python scripts/gen_widget.py
	zensical serve
