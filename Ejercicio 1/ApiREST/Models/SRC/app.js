const express = require('express');
const taskRoutes = require('./routes/task.routes');
const errorMiddleware = require('./middlewares/error.middleware');

const app = express();

app.use(express.json());

app.use('/api/tasks', taskRoutes);

// Middleware de errores SIEMPRE al final
app.use(errorMiddleware);

module.exports = app;