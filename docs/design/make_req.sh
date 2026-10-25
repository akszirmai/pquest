#!/bin/sh

java -jar ~/bin/plantuml-1.2026.8.jar ~/mystuff/workspace/python/pquest/docs/design/PQU_UseCase_model.puml

mv ~/mystuff/workspace/python/pquest/docs/design/PQU_UseCase_model.png ~/mystuff/workspace/python/pquest/docs/design/generated/

echo "Use Case diagram generation is completed."

python3 ~/mystuff/workspace/python/pquest/tools/reqgen.py ~/mystuff/workspace/python/pquest/docs/design/PQU_requirement_list.csv > ~/mystuff/workspace/python/pquest/docs/design/generated/PQU_requirement_list.adoc

echo "Requirements table has been processed and moved"

asciidoctor-pdf -a pdf-theme=PQU_pdf_doc_theme.yml ~/mystuff/workspace/python/pquest/docs/design/PQU_requirements.adoc

echo "PDF generation is completed"

explorer.exe PQU_requirements.pdf
