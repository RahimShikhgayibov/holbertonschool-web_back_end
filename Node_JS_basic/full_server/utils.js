import fs from 'fs';

/**
 * Asynchronously reads the database CSV file.
 * @param {string} filePath - Path to the CSV file.
 * @returns {Promise<Object>} Resolves with an object containing arrays of firstnames per field.
 */
export const readDatabase = (filePath) => new Promise((resolve, reject) => {
  if (!filePath) {
    reject(new Error('Cannot load the database'));
    return;
  }

  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    if (lines.length <= 1) {
      resolve({});
      return;
    }

    const studentRows = lines.slice(1);
    const fields = {};

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
        }
      }
    }

    resolve(fields);
  });
});

export default readDatabase;
