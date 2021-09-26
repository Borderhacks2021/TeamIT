import openpyxl

from datastore.models import WorkingGenius


FILEPATH = "Rolecall/Completed Databases/Working Genius Summary Database.xlsx"
def import_working_genius_data():
    
    workbook = openpyxl.load_workbook(FILEPATH)
    
    worksheet = workbook.active

    for row in worksheet.iter_rows(1, values_only=True):    
        if row[0]=="Input":
            continue
        elif row[0] is None:
            break
        else:
            WorkingGenius.objects.get_or_create(
                input=row[0],
                genius=row[1],
                definition=row[2],
                category=row[3],
                type=row[4]
            )
