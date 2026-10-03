const API_URL = `http://${window.location.hostname}:8000`;


function printTask(category, title, date) {
    fetch(`${API_URL}/request`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            heading: category,
            subheading: "ACTION REQUIRED",
            receipt_no: "000123",
            footer_note: "KEEP THIS RECEIPT",
            footer_shout: "GET IT DONE",
            task: {
                title: title,
                created_text: date,
                priority: "high",
                project: "Operations",
                is_overdue: false,
                due_text: "25 SEP 2026",
                assignee: "Mojito",
                ticket: "OPS-42",
                tags: ["printer", "office"],
                notes: "Use the 80 mm thermal roll.",
                subtasks: ["Order paper", "Install roll", "Print test receipt"],
            },
        })
    })
}

function addTask() {
    let category = document.getElementById("category").value;
    let subcategory = document.getElementById("subcategory").value;
    let title = document.getElementById("task-name").value;
    let today = getToday()
    let due = getDate(document.getElementById("due-date").value);
    let notes = document.getElementById("notes").value;

    // need to update this signature / endpoint
    printTask(category, title, today, subcategory);
}

function getDate(value) {
    if (!value) return "";

    const [year, month, day] = value.split("-").map(Number);
    return new Intl.DateTimeFormat("en-GB", {
        day: "numeric",
        month: "short",
        year: "numeric"
    }).format(new Date(year, month - 1, day));
}

function getToday() {
    let date = new Date();

    let formattedDate = new Intl.DateTimeFormat("en-GB", {
        day: "numeric",
        month: "short",
        year: "numeric"
    }).format(date);

    return formattedDate;
}