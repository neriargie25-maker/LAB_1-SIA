const express = require('express');
const axios = require('axios');
const path = require('path');
const fs = require('fs');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, '..')));

const LOG_FILE = path.join(__dirname, 'history.csv');
if (!fs.existsSync(LOG_FILE)) {
    fs.writeFileSync(LOG_FILE, 'timestamp,num1,num2,operation,result\n');
}

function logEntry(data, result) {
    const line = `${new Date().toISOString()},${data.num1},${data.num2},${data.operation},"${result}"\n`;
    fs.appendFileSync(LOG_FILE, line);
}

app.post('/api/calculate', async (req, res) => {
    try {
        const pyRes = await axios.post('http://localhost:5001/calculate', req.body);
        logEntry(req.body, pyRes.data.result);
        res.json(pyRes.data);
    } catch (err) {
        res.status(500).json({ error: 'Cannot reach Python service' });
    }
});

app.listen(3000, () => {
    console.log('✅ Node.js running on http://localhost:3000');
});