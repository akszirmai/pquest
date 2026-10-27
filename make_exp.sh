#!/bin/sh

PPATH="$HOME/mystuff/workspace/python/pquest"
DOCPATH=$PPATH/docs/development

asciidoctor-pdf -B docs/development -a pdf-themesdir="$PPATH"/docs/ -a pdf-theme=PQU_pdf_doc_theme.yml "$DOCPATH"/PQU_development.adoc

mv "$DOCPATH"/PQU_development.pdf "$DOCPATH"/generated

echo "Development Document PDF generation is completed. PDF is moved to the generated/ directory"

PDF_PATH="$DOCPATH"/generated/PQU_development.pdf
explorer.exe "$(wslpath -w "$PDF_PATH")"
