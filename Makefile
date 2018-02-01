all: build

build:
	urubu build

serve:
	cd _build && python -m http.server 8000

clean:
	rm -rf _build/* .*~
