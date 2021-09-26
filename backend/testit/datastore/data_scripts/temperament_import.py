import openpyxl

from datastore.models import TemparementSummary


FILEPATH = "Rolecall/Completed Databases/Temperaments Summary Database.xlsx"
def import_temperaments_data():
    
    workbook = openpyxl.load_workbook(FILEPATH)
    
    worksheet = workbook.active

    for row in worksheet.iter_rows(1, values_only=True):    
        if row[0]=="Type":
            continue
        elif row[0] is None:
            break
        else:
            TemparementSummary.objects.get_or_create(
                type=row[0],
                summary=row[1]
            )