TEXFILES = $(wildcard *.tex)
PDFFILES = $(TEXFILES:.tex=.pdf)

all: pdf

pdf: $(PDFFILES)

%.pdf: %.tex %-caso?.txt
	@rubber --pdf $<
clean:
	@rubber --clean --pdf $(TEXFILES:.tex=)

.PHONY: pdf clean all

