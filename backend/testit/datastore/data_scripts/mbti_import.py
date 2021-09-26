import openpyxl

from datastore.models import MBTISummary


FILEPATH = "Rolecall/Completed Databases/Myers Briggs Summary Database.xlsx"
def import_mbti_data():
    
    workbook = openpyxl.load_workbook(FILEPATH)
    
    worksheet = workbook.active

    for row in worksheet.iter_rows(1, values_only=True):    
        if row[0]=="Type":
            continue
        elif row[0] is None:
            break
        else:
            MBTISummary.objects.get_or_create(
                type=row[0],
                summary=row[1]
            )