import { readDatabase } from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const dbFile = process.argv[2];

    return readDatabase(dbFile)
      .then((fields) => {
        const responseParts = ['This is the list of our students'];

        const sortedFields = Object.keys(fields).sort((a, b) => (
          a.localeCompare(b, undefined, { sensitivity: 'base' })
        ));

        for (const field of sortedFields) {
          const names = fields[field];
          responseParts.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }

        return response.status(200).send(responseParts.join('\n'));
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      return response.status(500).send('Major parameter must be CS or SWE');
    }

    const dbFile = process.argv[2];

    return readDatabase(dbFile)
      .then((fields) => {
        const studentList = fields[major] || [];
        return response.status(200).send(`List: ${studentList.join(', ')}`);
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }
}

export default StudentsController;
