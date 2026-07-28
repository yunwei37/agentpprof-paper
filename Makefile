# Makefile for LaTeX compilation

# Main document (without .tex extension)
MAIN = main

# LaTeX compiler
LATEX = pdflatex
BIBTEX = bibtex

# All source files
TEXFILES = $(wildcard *.tex) $(wildcard figures/*.tex)
FIGURES = $(wildcard figures/*.pdf) $(wildcard figures/*.png)

.PHONY: all clean distclean

all: $(MAIN).pdf

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
