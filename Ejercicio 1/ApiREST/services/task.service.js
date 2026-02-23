let tasks = [];
let idCounter = 1;

// GET ALL
exports.getAll = () => {
    return tasks;
};

// GET BY ID
exports.getById = (id) => {
    return tasks.find(task => task.id === parseInt(id));
};

// CREATE
exports.create = (data) => {
    const newTask = {
        id: idCounter++,
        title: data.title,
        completed: data.completed || false
    };

    tasks.push(newTask);
    return newTask;
};

// UPDATE
exports.update = (id, data) => {
    const task = tasks.find(task => task.id === parseInt(id));
    if (!task) return null;

    task.title = data.title ?? task.title;
    task.completed = data.completed ?? task.completed;

    return task;
};

// DELETE
exports.remove = (id) => {
    const index = tasks.findIndex(task => task.id === parseInt(id));
    if (index === -1) return false;

    tasks.splice(index, 1);
    return true;
};