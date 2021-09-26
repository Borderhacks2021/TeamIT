
import openpyxl

from datastore.models import TemparementSummary
from employee.models import  EmployeeColourTraits


FILEPATH = "Rolecall/Completed Databases/Colour Traits Database.xlsx"
def import_employee_colour_traits_data():
    sanguine = TemparementSummary.objects.get(type="Sanguine")
    choleric = TemparementSummary.objects.get(type="Choleric")
    melancholic = TemparementSummary.objects.get(type="Melancholic")
    phlegmatic = TemparementSummary.objects.get(type="Phlegmatic")


    workbook = openpyxl.load_workbook(FILEPATH)


    for sheet in workbook.worksheets:

    # Define variable to read the active sheet:
        worksheet = workbook[sheet.title]

        for row in worksheet.iter_rows(1, values_only=True):
            if row[0]=="CTID Code":
                continue
            elif row[0] is None:
                break
            else:
                colour = "GREEN" if row[0][-1] == "g" else "RED"
                score = int(row[2]) if row[2] else 1
                EmployeeColourTraits.objects.create(
                    employee_id=sheet.title,
                    ctid_code=row[0],
                    temparement=sanguine,
                    trait=row[1],
                    score=score,
                    colour=colour
                )
                colour = "GREEN" if row[3][-1] == "g" else "RED"
                score = int(row[5]) if row[5] else 1
                EmployeeColourTraits.objects.create(
                    employee_id=sheet.title,
                    ctid_code=row[3],
                    temparement=choleric,
                    trait=row[4],
                    score=score,
                    colour=colour
                )
                colour = "GREEN" if row[6][-1] == "g" else "RED"
                score = int(row[8]) if row[8] else 1
                EmployeeColourTraits.objects.create(
                    employee_id=sheet.title,
                    ctid_code=row[6],
                    temparement=melancholic,
                    trait=row[7],
                    score=score,
                    colour=colour
                )
                colour = "GREEN" if row[9][-1] == "g" else "RED"
                score = int(row[11]) if row[11] else 1
                EmployeeColourTraits.objects.create(
                    employee_id=sheet.title,
                    ctid_code=row[9],
                    temparement=phlegmatic,
                    trait=row[10],
                    score=score,
                    colour=colour
                )