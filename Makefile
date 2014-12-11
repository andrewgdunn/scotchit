readme.pdf: readme.md readme.bib Makefile
	pandoc readme.md \
	-o readme.pdf \
	# --csl ieee-with-url.csl \
	--biblio readme.bib \
	-V geometry:margin=0.75in

clean:
	rm *.pdf