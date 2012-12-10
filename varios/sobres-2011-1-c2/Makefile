all: sobres.pdf
%.tex: %.py %.csv
	python $<
%.pdf: %.tex
	rubber --pdf $<
clean:
	-rm -f *.pdf *.tex *.aux *.log
