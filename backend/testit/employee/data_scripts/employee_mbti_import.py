import openpyxl

from datastore.models import MBTISummary
from employee.models import EmployeeMBTI

FILEPATH = "Rolecall/Completed Databases/Myers Briggs Results Database.xlsx"


def get_mbit_value(row):
    mbit_value = ""
    if int(row[1]):
        mbit_value+="E"
    if int(row[2]):
        mbit_value+="I"
    if int(row[3]):
        mbit_value+="N"
    if int(row[4]):
        mbit_value+="S"
    if int(row[5]):
        mbit_value+="F"
    if int(row[6]):
        mbit_value+="T"
    if int(row[7]):
        mbit_value+="J"
    if int(row[8]):
        mbit_value+="P"
    
    return mbit_value


def import_employee_mbti_data():

    workbook = openpyxl.load_workbook(FILEPATH)

    # Define variable to read the active sheet:
    worksheet = workbook.active

    for row in worksheet.iter_rows(values_only=True):
        if row[0]=="Employee ID":
            continue
        elif row[0] is None:
            break
        else:
            value = get_mbit_value(row)
            mbti = MBTISummary.objects.get(type=value)
            EmployeeMBTI.objects.get_or_create(
                employee_id=row[0],
                mbti=mbti
            )
