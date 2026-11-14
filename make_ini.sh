#!/bin/sh

PPATH="$HOME/mystuff/workspace/python/pquest"
DOCPATH=$PPATH/docs/initiation

asciidoctor-pdf -B docs/design -a pdf-themesdir="$PPATH"/docs/ -a pdf-theme=PQU_pdf_doc_theme.yml "$DOCPATH"/PQU_dev_envir.adoc

mv "$DOCPATH"/PQU_dev_envir.pdf "$DOCPATH"/generated

echo "PDF generation is completed. PDF is moved to the generated/ directory"

PDF_PATH="$DOCPATH"/generated/PQU_dev_envir.pdf
explorer.exe "$(wslpath -w "$PDF_PATH")"
