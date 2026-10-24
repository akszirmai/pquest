#!/bin/sh

java -jar ~/bin/plantuml-1.2026.8.jar ~/mystuff/workspace/python/pquest/docs/design/PQU_class_model.puml

mv ~/mystuff/workspace/python/pquest/docs/design/PQU_class_model.png ~/mystuff/workspace/python/pquest/docs/design/generated/

echo "Class diagram generation is completed."

asciidoctor-pdf -a pdf-theme=PQU_pdf_doc_theme.yml ~/mystuff/workspace/python/pquest/docs/design/PQU_sys_design.adoc

echo "PDF generation is completed"

mv ~/mystuff/workspace/python/pquest/docs/design/PQU_sys_design.pdf ./generated

echo "PDF is copied to ./generated"

explorer.exe $(wslpath -w generated/PQU_sys_design.pdf)
