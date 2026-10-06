const API_URL = `http://${window.location.hostname}:8000`;


function printTask(category, title, today, due, notes, priority, subcategory, project) {
    fetch(`${API_URL}/request`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            heading: category,
            subheading: subcategory,
            receipt_no: "000123",
            footer_note: "KEEP THIS RECEIPT",
            footer_shout: "GET IT DONE",
            task: {
                title: title,
                created_text: today,
                priority: priority,
                project: project,
                is_overdue: false,
                due_text: due,
                notes: notes,
                subtasks: ["Order paper", "Install roll", "Print test receipt"],
            },
        })
    })
}

function addTask() {
    let category = document.getElementById("category");
    category = category.options[category.selectedIndex]?.text;    
    let subcategory = document.getElementById("subcategory");
    subcategory = subcategory.options[subcategory.selectedIndex]?.text;
    let project = document.getElementById("project");
    project = project.options[project.selectedIndex]?.text;
    let title = document.getElementById("task-name").value;
    let today = getToday()
    let due = getDate(document.getElementById("due-date").value);
    let notes = document.getElementById("notes").value;
    let priority = document.getElementById("priority").value;

    // need to update this signature / endpoint
    printTask(category, title, today, due, notes, priority, subcategory, project);
}

function addSubTask() {
    // add text box into subtask div above button, naming subtask(n) based on number - or a group
    
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

