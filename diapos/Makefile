TEXDIAPOS = $(wildcard *-diapos.tex)
TEXNOTAS  = $(wildcard *-notas.tex)
PDFDIAPOS = $(TEXDIAPOS:.tex=.pdf)
PDFNOTAS  = $(TEXNOTAS:.tex=.pdf)

pdf: $(PDFDIAPOS) $(PDFNOTAS)

%.pdf: %.tex
	@rubber --pdf $<
clean:
	@rubber --clean --pdf $(TEXFILES:.tex=)
	@rm -f *.vrb

.PHONY: pdf clean
