# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =

PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -q -d _build/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

DEPLOYDIR = $(HOME)/public_html/progra
OPEN = xdg-open

.PHONY: all help clean html latex deploy diagramas diapos open

all: html

diagramas:
	-$(MAKE) -C diagramas
diapos:
	-$(MAKE) -C diapos

open:
	@$(OPEN) _build/html/index.html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"

clean:
	-rm -rf _build/*

html: diagramas
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) _build/html
	sh scripts/fix-testcases.sh
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) _build/latex
	@echo
	@echo "Build finished; the LaTeX files are in _build/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

deploy: html
	@if [ $$(hostname | cut -d. -f2-) = csrg.inf.utfsm.cl ]; \
	then \
	    echo "Deploying to $(DEPLOYDIR)"; \
	    rm -rf "$(DEPLOYDIR)"; \
	    cp -R _build/html/ "$(DEPLOYDIR)"; \
	else \
	    echo "You must deploy from your csrg account"; \
	fi

