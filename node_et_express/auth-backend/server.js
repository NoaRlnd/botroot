const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(cors());

const db = mysql.createConnection({
    host: '172.22.0.230', // Remplacez par l'adresse IP de votre Raspberry Pi
    user: 'root',
    password: 'adminadmin.2025', // Remplacez par le mot de passe de votre utilisateur MariaDB
    database: 'auth_db'
});

db.connect((err) => {
    if (err) throw err;
    console.log('Connected to MariaDB');
});

app.post('/login', (req, res) => {
    console.log('Login request received:', req.body); // Ajout de journalisation
    const { username, password } = req.body;
    const query = 'SELECT * FROM users WHERE username = ? AND password = ?';
    db.query(query, [username, password], (err, results) => {
        if (err) throw err;
        if (results.length > 0) {
            res.json({ success: true, role: results[0].role });
            
        } else {
            res.json({ success: false });
        }
    });
});

app.post('/addUser', (req, res) => {
    console.log('Add user request received:', req.body); // Ajout de journalisation
    const { username, password, role } = req.body;
    const query = 'INSERT INTO users (username, password, role) VALUES (?, ?, ?)';
    db.query(query, [username, password, role], (err, results) => {
        if (err) throw err;
        res.json({ success: true });
    });
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});