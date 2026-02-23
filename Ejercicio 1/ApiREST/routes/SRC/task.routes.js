const express = require('express');
const { body, param } = require('express-validator');
const taskController = require('../controllers/task.controller');
const validate = require('../middlewares/validation.middleware');

const router = express.Router();

router.post(
  '/',
  [
    body('title')
      .notEmpty().withMessage('Title is required')
      .isLength({ min: 3 }).withMessage('Title must be at least 3 characters'),
      
    body('completed')
      .optional()
      .isBoolean().withMessage('Completed must be boolean')
  ],
  validate,
  taskController.createTask
);

router.get('/:id',
  [
    param('id')
      .isInt().withMessage('ID must be a number')
  ],
  validate,
  taskController.getTaskById
);

module.exports = router;