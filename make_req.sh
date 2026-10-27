#!/bin/sh

PPATH="$HOME/mystuff/workspace/python/pquest"
DOCPATH=$PPATH/docs/design

java -jar ~/bin/plantuml-1.2026.8.jar "$DOCPATH"/PQU_UseCase_model.puml

mv "$DOCPATH"/PQU_UseCase_model.png "$DOCPATH"/generated/

echo "Use Case diagram generation is completed."

python3 "$PPATH"/tools/reqgen.py "$DOCPATH"/PQU_requirement_list.csv > "$DOCPATH"/generated/PQU_requirement_list.adoc

echo "Requirements table has been processed and moved"

asciidoctor-pdf -B docs/design -a pdf-themesdir="$PPATH"/docs/ -a pdf-theme=PQU_pdf_doc_theme.yml "$DOCPATH"/PQU_requirements.adoc

mv "$DOCPATH"/PQU_requirements.pdf "$DOCPATH"/generated

echo "PDF generation is completed. PDF is moved to the generated/ directory"

PDF_PATH="$DOCPATH"/generated/PQU_requirements.pdf
explorer.exe "$(wslpath -w "$PDF_PATH")"
