import openpyxl

from employee.models import Employee
# Define variable to load the wookbook

FILEPATH = "Rolecall/Completed Databases/Employee Registry Database.xlsx"
def import_employee_data():

    workbook = openpyxl.load_workbook(FILEPATH)

    # Define variable to read the active sheet:
    worksheet = workbook.active

    for row in worksheet.iter_rows(values_only=True):
        if row[0]=="Employee ID":
            continue
        elif row[0] is None:
            break
        else:
            Employee.objects.get_or_create(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                department=row[3].upper(),
                role=row[4],
                hourly_rate=row[5]
            )
