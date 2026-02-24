const taskService = require('../services/task.service');

// GET ALL
exports.getAllTasks = (req, res) => {
    const tasks = taskService.getAll();
    res.json(tasks);
};

// GET BY ID
exports.getTaskById = (req, res) => {
    const task = taskService.getById(req.params.id);

    if (!task) {
        return res.status(404).json({ message: 'Tarea no encontrada' });
    }

    res.json(task);
};

// POST
exports.createTask = (req, res) => {
    const newTask = taskService.create(req.body);
    res.status(201).json(newTask);
};

// PUT
exports.updateTask = (req, res) => {
    const updatedTask = taskService.update(req.params.id, req.body);

    if (!updatedTask) {
        return res.status(404).json({ message: 'Tarea no encontrada' });
    }

    res.json(updatedTask);
};

// DELETE
exports.deleteTask = (req, res) => {
    const deleted = taskService.remove(req.params.id);

    if (!deleted) {
        return res.status(404).json({ message: 'Tarea no encontrada' });
    }

    res.json({ message: 'Tarea eliminada correctamente' });
};