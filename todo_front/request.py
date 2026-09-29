import requests

data = {
    "heading": "CLEANING",
    "subheading": "Kitchen",
    "receipt_no": "000465",
    "footer_note": "-",
    "footer_shout": "",
    "task": {
        "title": "Clean Oven",
        "created_text": "24 SEP 2026",
        "priority": "medium",
        "project": "Rituals",
        "is_overdue": False,
        "due_text": "25 SEP 2026",
        "assignee": "Alex",
        "ticket": "9",
        "tags": ["kitchen", "cleaning", "deep clean"],
        "notes": "remove oven door, soak grates",
    },
}

response = requests.post(
    "http://localhost:8000/request",
    json=data


)
