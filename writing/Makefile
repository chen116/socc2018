FILE=socc2018
# OUTNAME=ISPA2017_cam_ready
FLAGS=--file-line-error --synctex=1
preview=open -a /Applications/Preview.app
upreview=xpdf

all:
	rm -f *~ *.dvi *.aux *.log *.bbl *.blg *.out *.toc *.spl *.synctex.gz
	/Library/TeX/texbin/pdflatex ${FLAGS} ${FILE}
	/Library/TeX/texbin/bibtex ${FILE}
	/Library/TeX/texbin/pdflatex ${FLAGS} ${FILE}
	/Library/TeX/texbin/pdflatex ${FLAGS} ${FILE}
	# cp ${FILE}.pdf ${OUTNAME}.pdf
	make -f Makefile view
newv:
	cp ${FILE}.pdf ${OUTNAME}.pdf


simple:
	pdflatex ${FLAGS} ${FILE}
	make -f Makefile view

mimetype:
	svn propset svn:mime-type "application/pdf" *.pdf
	svn commit -m "fixed mimetype"

clean:
	rm -f *~ *.dvi *.aux *.log *.bbl *.blg *.out *.toc *.spl *.synctex.gz

view:
	${preview} ${FILE}.pdf

uview:
	${upreview} ${FILE}.pdf

acro:
#	gv ${FILE}.pdf
	killall AdobeReader
	open ${FILE}.pdf

gv:
	gv ${FILE}.pdf

bib-duplicate:
	echo "CHECKING FOR DUPLICATED ENTRIES"
	bibtool -d ../bib/*.bib *.bib | fgrep -v "non-space" > bib.log

bib-extract:
	echo "EXTRACTING ALL USED CITATIONS INTO A BIB FILE"
	bibtool -x ${FILE}.aux -o ${FILE}.bib
