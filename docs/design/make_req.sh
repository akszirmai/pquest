#!/bin/sh

python3 ~/mystuff/workspace/python/pquest/tools/reqgen.py PQU_requirement_list.csv > ~/mystuff/workspace/python/pquest/docs/design/generated/PQU_requirement_list.adoc

echo "table generation is completed."

asciidoctor-pdf -a pdf-theme=PQU_pdf_doc_theme.yml ~/mystuff/workspace/python/pquest/docs/design/PQU_requirements.adoc

echo "PDF generation is completed"

mv ~/mystuff/workspace/python/pquest/docs/design/PQU_requirements.pdf ./generated

echo "PDF is copied to ./generated"

explorer.exe $(wslpath -w generated/PQU_requirements.pdf)
