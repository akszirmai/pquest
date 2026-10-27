#!/bin/sh

PPATH="$HOME/mystuff/workspace/python/pquest"
DOCPATH=$PPATH/docs/design

java -jar ~/bin/plantuml-1.2026.8.jar $DOCPATH/PQU_class_model.puml

mv $DOCPATH/PQU_class_model.png $DOCPATH/generated/

echo "Class diagram generation is completed."

#asciidoctor-pdf -B docs/design -a pdf-themesdir="$PPATH"/docs/ -a pdf-theme=PQU_pdf_doc_theme.yml $DOCPATH/PQU_sys_design.adoc
#-a imagesoutdir="$DOCPATH"

asciidoctor-pdf -r asciidoctor-mathematical -B "$(realpath "$DOCPATH")" -a imagesoutdir="$(realpath "$DOCPATH")/generated" -a pdf-themesdir="$PPATH"/docs/ -a pdf-theme=PQU_pdf_doc_theme.yml "$DOCPATH"/PQU_sys_design.adoc

echo "PDF generation is completed"

mv $DOCPATH/PQU_sys_design.pdf $DOCPATH/generated

echo "PDF is copied to ./generated"

PDF_PATH="$PPATH"/docs/design/generated/PQU_sys_design.pdf
explorer.exe "$(wslpath -w "$PDF_PATH")"
