all: build

build:
	urubu build

serve:
	python _python/serve.py

clean:
	rm -rf _build/* .*~
