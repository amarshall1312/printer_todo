const API_URLdata = `http://${window.location.hostname}:8000`;


async function loadCategories() {
    const response = await fetch(`${API_URLdata}/categories`);

    if (!response.ok) {
        throw new Error("Failed to load categories");
    }

    const categories = await response.json();

    const dropdown = document.getElementById("category");
    console.log("getting categories")
    categories.forEach(category => {
        const option = document.createElement("option");

        option.value = category.category_id;
        option.textContent = category.name;

        dropdown.appendChild(option);
    });

}

async function loadSubcategories(categoryId) {
    const response = await fetch(
        `${API_URLdata}/subcategories?category_id=${categoryId}`
    );

    if (!response.ok) {
        throw new Error("Failed to load subcategories");
    }

    const subcategories = await response.json();

    const dropdown = document.getElementById("subcategory");

    // Remove old subcategories
    dropdown.innerHTML = "";

    subcategories.forEach(subcategory => {
        const option = document.createElement("option");

        option.value = subcategory.subcategory_id;
        option.textContent = subcategory.name;

        dropdown.appendChild(option);
    });

}

async function loadProjects() {
    const response = await fetch(`${API_URLdata}/projects`);

    if (!response.ok) {
        throw new Error("Failed to load projects");
    }

    const projects = await response.json();

    const dropdown = document.getElementById("project");
    console.log("getting projects")
    projects.forEach(project => {
        const option = document.createElement("option");

        option.value = project.project_id;
        option.textContent = project.name;

        dropdown.appendChild(option);
    });

}

document.addEventListener("DOMContentLoaded", () => {
    const categoryDropdown = document.getElementById("category");

    categoryDropdown.addEventListener("change", () => {
        loadSubcategories(categoryDropdown.value);
    });

    loadCategories();
    loadProjects();

});