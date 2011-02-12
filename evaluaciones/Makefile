TEXFILES = $(wildcard *.tex)
PDFFILES = $(TEXFILES:.tex=.pdf)

all: pdf

pdf: $(PDFFILES)

%.pdf: %.tex ../latex/* %/*
	@rubber --pdf $<
clean:
	@rubber --clean --pdf $(TEXFILES:.tex=)

.PHONY: pdf clean all

