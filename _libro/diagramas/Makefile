TEXFILES = $(wildcard *.tex)
PDFFILES = $(TEXFILES:.tex=.pdf)
PNGFILES = $(PDFFILES:.pdf=.png)
GIFFILES = multiplicacion.gif

all: png gif

png: $(PNGFILES)
pdf: $(PDFFILES)
gif: $(GIFFILES)

multiplicacion.png: multiplicacion.pdf
	@# no hacer nada
multiplicacion.gif: multiplicacion.pdf
	@echo "creating $@..."
	@convert -density 400 -quality 80 -loop 0 \
	     -delay 300 '$<[0]'    \
	     -delay 50  '$<[1-22]' \
	     -delay 300 '$<[23]'   \
	     -scale 30\% $@

%.pdf: %.tex
	@rubber --pdf $<
%.png: %.pdf
	@echo "creating $@..."
	@convert -density 1200 -scale 10\% -quality 80 $< $@
clean:
	@rubber --clean --pdf $(TEXFILES:.tex=)
	@rm -f *.png *.gif *.vrb

.PHONY: png pdf clean all

