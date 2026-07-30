# Makefile for LaTeX compilation

# Main document (without .tex extension)
MAIN = main

# LaTeX compiler
LATEX = pdflatex
BIBTEX = bibtex

# All source files
TEXFILES = $(wildcard *.tex) $(wildcard figures/*.tex)
FIGURES = $(wildcard figures/*.pdf) $(wildcard figures/*.png)

.PHONY: all clean distclean arxiv

all: $(MAIN).pdf

# arXiv submission: include .bbl (pre-built), source, figures, style files
arxiv: $(MAIN).bbl
	rm -rf arxiv-submit arxiv-submit.tar.gz
	mkdir -p arxiv-submit
	cp $(MAIN).tex $(MAIN).bbl references.bib arxiv-submit/
	cp aaai2027.sty aaai2027.bst arxiv-submit/
	cp -r figures arxiv-submit/
	cd arxiv-submit && tar -czvf ../arxiv-submit.tar.gz .
	rm -rf arxiv-submit
	@echo "Created arxiv-submit.tar.gz"

# Full build: pdflatex -> bibtex -> pdflatex x2 resolves citations and refs
# from a clean checkout (no .bbl is committed).
$(MAIN).pdf: $(MAIN).tex $(TEXFILES) $(FIGURES) references.bib
	$(LATEX) $(MAIN)
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)

clean:
	rm -f *.aux *.log *.bbl *.blg *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz comment.cut

distclean: clean
	rm -f $(MAIN).pdf
