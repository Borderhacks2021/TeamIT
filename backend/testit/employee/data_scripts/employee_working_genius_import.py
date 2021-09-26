import openpyxl

# from datastore.models import MBTISummary
from employee.models import EmployeeWorkingGenius
from datastore.models import WorkingGenius

FILEPATH = "Rolecall/Completed Databases/Working Genius Results Database.xlsx"


def import_employee_working_genius_data():

    workbook = openpyxl.load_workbook(FILEPATH)

    # Define variable to read the active sheet:
    worksheet = workbook.active

    for row in worksheet.iter_rows(values_only=True):
        if row[0]=="Employee ID":
            continue
        elif row[0] is None:
            break
        else:
            wg_p = WorkingGenius.objects.get(input=row[1])
            wg_s = WorkingGenius.objects.get(input=row[2])
            wc_p = WorkingGenius.objects.get(input=row[3])
            wc_s = WorkingGenius.objects.get(input=row[4])
            wf_p = WorkingGenius.objects.get(input=row[5])
            wf_s = WorkingGenius.objects.get(input=row[6])
            EmployeeWorkingGenius.objects.create(
                employee_id=row[0],
                wg_primary=wg_p,
                wg_secondary=wg_s,
                wc_primary=wc_p,
                wc_secondary=wc_s,
                wf_primary=wf_p,
                wf_secondary=wf_s
            )
