import openpyxl

# from employee.models import Employee
from datastore.models import Program
# Define variable to load the wookbook

FILEPATH = "Rolecall/Completed Databases/Programs Database.xlsx"
def import_program_data():
    
    workbook = openpyxl.load_workbook(FILEPATH)

    for sheet in workbook.worksheets:

    # Define variable to read the active sheet:
        worksheet = workbook[sheet.title]

        for row in worksheet.iter_rows(1, values_only=True):
            if row[0]=="Employee ID":
                continue
            else:
                Program.objects.get_or_create(
                    program_id=row[1],
                    program_name=sheet.title
                )
                break