import rdflib
from pyshacl import validate

# 1. Define your file paths
data_file = "long-term-knb-vision/rdf-data/sample/data_mortgage.ttl"
ontology_file = "long-term-knb-vision/ontologies/Mortgage.ttl"
shapes_file = "long-term-knb-vision/shapes/shapes.ttl"

# 2. Load the graphs
data_graph = rdflib.Graph()
data_graph.parse(data_file, format="turtle")

ontology_graph = rdflib.Graph()
ontology_graph.parse(ontology_file, format="turtle")

shapes_graph = rdflib.Graph()
shapes_graph.parse(shapes_file, format="turtle")

# 3. Perform Validation
# 'ont_graph' allows SHACL to see the class hierarchy (e.g., PersoonPartij is a Partij)
# 'inference' can be 'rdfs', 'owlrl', etc.
conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shapes_graph,
    ont_graph=ontology_graph,
    inference='both', 
    abort_on_first=False,
    serialize_report_graph=True
)

# 4. Output the results
if conforms:
    print("✅ Validation Successful: The data conforms to the mortgage shapes.")
else:
    print("❌ Validation Failed:")
    print(results_text)

# Optional: Save the validation report to a file
# results_graph.serialize(destination='validation_report.ttl', format='turtle')