# You can set these variables from the command line.
SPHINXBUILD   = sphinx-build
ALLSPHINXOPTS = -q -d _build/doctrees .

DEPLOYDIR = crux:progra.usm.cl/apunte
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
#	rsync -a _build/html/ $(DEPLOYDIR)
	aws s3 cp _build/html s3://progra.cl/ --recursive --profile progra.cl

