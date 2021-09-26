import openpyxl
from employee.models import Employee, EmployeeProgramSkills


FILEPATH = "Rolecall/Completed Databases/Programs Database.xlsx"
def import_employee_program_data():
    
    workbook = openpyxl.load_workbook(FILEPATH)

    for sheet in workbook.worksheets:

    # Define variable to read the active sheet:
        worksheet = workbook[sheet.title]

        for row in worksheet.iter_rows(1, values_only=True):
            if row[0]=="Employee ID":
                continue
            elif row[0] is None:
                break
            else:
                employee = Employee.objects.get(id=row[0])
                EmployeeProgramSkills.objects.get_or_create(
                    employee=employee,
                    program_id=row[1],
                    level=int(row[2])
                )