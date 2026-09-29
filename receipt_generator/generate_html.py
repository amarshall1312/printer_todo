from pathlib import Path

from jinja2 import Environment, FileSystemLoader


TEMPLATE_DIR = Path("templates")
OUTPUT_PATH = Path("output/html/receipt.html")


def render_receipt(context: dict, output_path: str | Path = OUTPUT_PATH) -> Path:
    """Render receipt.html with receipt content and save the resulting HTML."""
    template = Environment(loader=FileSystemLoader(TEMPLATE_DIR)).get_template(
        "receipt.html"
    )
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template.render(**context), encoding="utf-8")
    return output_path


if __name__ == "__main__":
    receipt = {
        "heading": "TASK RECEIPT",
        "subheading": "ACTION REQUIRED",
        "receipt_no": "000123",
        "footer_note": "KEEP THIS RECEIPT",
        "footer_shout": "GET IT DONE",
        "task": {
            "title": "Replace printer paper",
            "created_text": "24 SEP 2026",
            "priority": "high",
            "project": "Operations",
            "is_overdue": False,
            "due_text": "25 SEP 2026",
            "assignee": "Mojito",
            "ticket": "OPS-42",
            "tags": ["printer", "office"],
            "notes": "Use the 80 mm thermal roll.",
            "subtasks": ["Order paper", "Install roll", "Print test receipt"],
        },
    }

    print(render_receipt(receipt))