const express = require('express');
const fs = require('fs');

const app = express();
const PORT = 1245;
const DB_FILE = process.argv[2];

/**
 * Reads student database asynchronously and resolves with formatted output string.
 * @param {string} path - Path to the CSV database file.
 * @returns {Promise<string>}
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    if (!path) {
      reject(new Error('Cannot load the database'));
      return;
    }

    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }

      const studentRows = lines.slice(1);
      const fields = {};
      let totalStudents = 0;

      for (const row of studentRows) {
        const studentData = row.split(',');

        if (studentData.length >= 4) {
          const firstname = studentData[0].trim();
          const field = studentData[3].trim();

          if (firstname && field) {
            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(firstname);
            totalStudents += 1;
          }
        }
      }

      let output = `Number of students: ${totalStudents}`;

      for (const [field, names] of Object.entries(fields)) {
        output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      }

      resolve(output);
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(DB_FILE)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((error) => {
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(PORT);

module.exports = app;
