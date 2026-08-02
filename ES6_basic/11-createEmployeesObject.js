export default function createEmployeesObject(departmentName, employees) {
  let empObj = {
    [departmentName]: employees,
  };

  return empObj;
}