const taskService = require('../services/task.service');

exports.createTask = async (req, res, next) => {
  try {
    const task = await taskService.create(req.body);

    return res.status(201).json({
      status: 'success',
      data: task
    });

  } catch (error) {
    next(error);
  }
};

exports.getTaskById = async (req, res, next) => {
  try {
    const task = await taskService.getById(req.params.id);

    if (!task) {
      return res.status(404).json({
        status: 'error',
        message: 'Task not found'
      });
    }

    return res.status(200).json({
      status: 'success',
      data: task
    });

  } catch (error) {
    next(error);
  }
};