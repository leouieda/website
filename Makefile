PY=python
PELICAN=pelican
PELICANOPTS=
CONDAENV=pelican
BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/conf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py


html: clean $(OUTPUTDIR)/index.html

help:
	@echo 'Usage:'
	@echo '   make html         (re)generate the web site'
	@echo '   make clean        remove the generated files'
	@echo '   make regenerate   regenerate files upon modification'
	@echo '   make publish      generate using production settings'
	@echo '   make serve        start a server in port 8001'
	@echo '   make setup        Create a conda env and install dependencies'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

debug:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -D

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete
	rm -f *.pyc
	rm -rf cache

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && $(PY) -m http.server 8001

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

setup: install_requires

mkenv:
	conda create -n $(CONDAENV) --yes pip python=3.4

install_requires: mkenv
	bash -c "source activate $(CONDAENV) && pip install -r requirements.txt"

delete_env:
	bash -c "source deactivate; conda env remove --name $(CONDAENV)"

.PHONY: html help clean regenerate publish serve
