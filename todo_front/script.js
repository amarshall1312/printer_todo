

function printTask(category, title) {
    fetch("http://localhost:8000/request", {
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
                created_text: "24 SEP 2026",
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
    let title = document.getElementById("task-name").value;
    console.log(title + category);
    printTask(category, title);
}