build:
	urubu build

serve:
	@urubu serve 2> /dev/null > /dev/null &

clean:
	rm -rf _build/* .*~
