const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

const connection = mysql.createConnection({
  host: 'localhost',  
  user: 'marcela', 
  password: 'BolaYAlina2611', 
  database: 'your-database' 
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Connected to the database!');
});

// Create
app.post('/items', (req, res) => {
  const { name, value } = req.body;
  connection.query('INSERT INTO items (name, value) VALUES (?, ?)', [name, value], (err, result) => {
    if (err) throw err;
    res.send('Item added!');
  });
});

// Read
app.get('/items', (req, res) => {
  connection.query('SELECT * FROM items', (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

// Update
app.put('/items/:id', (req, res) => {
  const { name, value } = req.body;
  const { id } = req.params;
  connection.query('UPDATE items SET name = ?, value = ? WHERE id = ?', [name, value, id], (err, result) => {
    if (err) throw err;
    res.send('Item updated!');
  });
});

// Delete
app.delete('/items/:id', (req, res) => {
  const { id } = req.params;
  connection.query('DELETE FROM items WHERE id = ?', [id], (err, result) => {
    if (err) throw err;
    res.send('Item deleted!');
  });
});

app.use(express.static('public'));

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
