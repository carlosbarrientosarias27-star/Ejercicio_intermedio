const express = require('express');
const app = express();
const taskRoutes = require('./routes/task.routes');

app.use(express.json());

app.use('/api/tasks', taskRoutes);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Servidor corriendo en puerto ${PORT}`);
});