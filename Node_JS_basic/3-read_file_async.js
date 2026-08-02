const fs = require('fs');

/**
 * Counts and logs student data asynchronously from a CSV file.
 * @param {string} path - Path to the CSV database file.
 * @returns {Promise<void>}
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split lines and filter out empty lines
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // If the file only contains headers or is empty
      if (lines.length <= 1) {
        console.log('Number of students: 0');
        resolve();
        return;
      }

      // Remove header line
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

      console.log(`Number of students: ${totalStudents}`);

      for (const [field, names] of Object.entries(fields)) {
        console.log(
          `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`,
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
