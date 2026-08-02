export default function updateGradeByCity(students, city, newGrades) {
    if (!Array.isArray(students) || !Array.isArray(newGrades)) {
        return [];
    }

    return students.filter((student) => student.location === city).map((student) => {
        const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
        if (gradeObj) {
            return { ...student, grade: gradeObj.grade };
        }
        return { ...student, grade: 'N/A' };
    });
}