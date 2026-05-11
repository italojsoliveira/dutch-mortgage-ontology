import rdflib
from pyshacl import validate

data_file = "results/01_ing_bank/data.ttl"
ontology_file = "gufo/Mortgage.ttl"
shapes_file = "ex/shapes.ttl"
report_file = "results/01_ing_bank/validation_report.txt"

data_graph = rdflib.Graph()
data_graph.parse(data_file, format="turtle")

ontology_graph = rdflib.Graph()
ontology_graph.parse(ontology_file, format="turtle")

shapes_graph = rdflib.Graph()
shapes_graph.parse(shapes_file, format="turtle")

conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shapes_graph,
    ont_graph=ontology_graph,
    inference='both',
    abort_on_first=False,
    serialize_report_graph=True
)

output_lines = []
if conforms:
    msg = "Validation Successful: The data conforms to the mortgage shapes."
    print(f"✅ {msg}")
    output_lines.append(msg)
else:
    print("❌ Validation Failed:")
    print(results_text)
    output_lines.append("Validation Failed:")
    output_lines.append(results_text)

with open(report_file, "w") as f:
    f.write("\n".join(output_lines))

with open("results/01_ing_bank/validation_report.ttl", "wb") as f:
    f.write(results_graph)

print(f"\nResults saved to {report_file}")
