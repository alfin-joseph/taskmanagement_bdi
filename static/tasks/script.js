document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('#task-list')) {
        fetchTasks();
    }

    if (document.querySelector('#add-task-form')) {
        document.querySelector('#add-task-form').addEventListener('submit', function(e) {
            e.preventDefault();
            addTask();
        });
    }

    if (document.querySelector('#edit-task-form')) {
        const taskId = new URLSearchParams(window.location.search).get('id');
        fetchTask(taskId);
        document.querySelector('#edit-task-form').addEventListener('submit', function(e) {
            e.preventDefault();
            updateTask(taskId);
        });
    }
});

function fetchTasks() {
    fetch('/tasks/')
        .then(response => response.json())
        .then(data => {
            const taskList = document.querySelector('#task-list');
            taskList.innerHTML = '';
            data.forEach(task => {
                const taskItem = document.createElement('div');
                taskItem.classList.add('task-item');
                taskItem.innerHTML = `
                    <h3>${task.title}</h3>
                    <p>${task.description}</p>
                    <p>Completed: ${task.completed}</p>
                    <button onclick="editTask(${task.id})">Edit</button>
                    <button onclick="deleteTask(${task.id})">Delete</button>
                `;
                taskList.appendChild(taskItem);
            });
        });
}

function addTask() {
    const title = document.querySelector('#title').value;
    const description = document.querySelector('#description').value;
    const completed = document.querySelector('#completed').checked;

    fetch('/tasks/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description, completed })
    }).then(response => {
        if (response.ok) {
            window.location.href = '/';
        }
    });
}

function fetchTask(id) {
    fetch(`/tasks/${id}/`)
        .then(response => response.json())
        .then(data => {
            document.querySelector('#task-id').value = data.id;
            document.querySelector('#title').value = data.title;
            document.querySelector('#description').value = data.description;
            document.querySelector('#completed').checked = data.completed;
        });
}

function updateTask(id) {
    const title = document.querySelector('#title').value;
    const description = document.querySelector('#description').value;
    const completed = document.querySelector('#completed').checked;

    fetch(`/tasks/${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description, completed })
    }).then(response => {
        if (response.ok) {
            window.location.href = '/';
        }
    });
}

function deleteTask(id) {
    fetch(`/tasks/${id}/`, {
        method: 'DELETE'
    }).then(response => {
        if (response.ok) {
            fetchTasks();
        }
    });
}

function editTask(id) {
    window.location.href = `/edit_task?id=${id}`;
}
