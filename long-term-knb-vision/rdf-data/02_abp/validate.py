from pathlib import Path
import rdflib
from pyshacl import validate

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent.parent

data_file = script_dir / "data.ttl"
ontology_file = project_root / "ontouml" / "experiment" / "test" / "Mortgage.ttl"
shapes_file = project_root / "shapes" / "mortgage-shapes.ttl"
report_txt = script_dir / "validation_report.txt"
report_ttl = script_dir / "validation_report.ttl"

data_graph = rdflib.Graph()
data_graph.parse(str(data_file), format="turtle")

ontology_graph = rdflib.Graph()
ontology_graph.parse(str(ontology_file), format="turtle")

shapes_graph = rdflib.Graph()
shapes_graph.parse(str(shapes_file), format="turtle")

conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shapes_graph,
    ont_graph=ontology_graph,
    inference="both",
    abort_on_first=False,
    serialize_report_graph=True,
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

with open(report_txt, "w") as f:
    f.write("\n".join(output_lines))

with open(report_ttl, "wb") as f:
    f.write(results_graph)

print(f"\nReports saved to {report_txt}")
