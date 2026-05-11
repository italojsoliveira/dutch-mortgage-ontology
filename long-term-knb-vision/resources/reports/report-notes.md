# Benefits

- Interoperability (other sources)
- Semantic clarity (conceptual clarification)
- Knowledge management (vocabulary, data, and metadata)
- Semantic infrastructure to support multiple services (better automation)
- Simplification of the infrastructure
- Multiple levels of data validation (correct deeds)

# Tech Stack

- OntoUML (Visual Paradigm, our preferred tool for conceptual modeling in OntoUML)
- gUFO (OWL 2 DL) - upper ontology
- GraphDB (triplestore) - a Graphwise's product
- SHACL (data validation)
- Regex, NER models, LLMs (information extraction)
- Web-based forms (ULB-Darmstadt/shacl-form)?
  - Unsure, since the deed generation can be performed based on the bank order (XML file)
  

Jan-Lyckle: One of the main things that is happening is that there are teams at basically every organisation in the chain that is concerning itself with manually reading pdf-documents, looking for the important data points and extracting them by hand to eventually compare it to the data they have themselves. Furthermore, there have been some attempts in standardizing mortgage templates with a stamp of originality, but this has not led to the desired results because the moment the notary wants to change anything, the stamp is revoked and the resulting deed needs to be manually checked as well.