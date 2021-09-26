from os import link
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from employee.models import Employee, EmployeeMBTI, EmployeeWorkingGenius, EmployeeColourTraits, EmployeeProgramSkills
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import PageBreak
from report.constants import SKILL_CODES
from django.db.models import Sum
from reportlab.rl_config import defaultPageSize
from datastore.models import Program

DOCUMENT_TITLE = "Employee Report"
CANVAS_FONT = "Times-Roman"


def get_skill_level(red_value, green_value):
    if (green_value <=12) and (red_value>=24):
        return "Entry"
    elif (green_value==18 and red_value == 18):
        return "Intermediate"
    elif (green_value >=12 and green_value<=18) and (red_value >=18 and red_value<=24):
        return "Basic"
    elif (green_value >=18 and green_value<=24) and (red_value >=12 and red_value<=18):
        return "Advanced"
    elif (green_value>=24) and (red_value<=12):
        return "Expert"
    else:
        return "UNKNOWN"

def generate_report(employee_code="RC004"):
    canvas = Canvas("employee_report.pdf", pagesize=LETTER)

    # Set font to Times New Roman with 12-point size
    canvas.setFont(CANVAS_FONT, 10)
    canvas.setTitle(DOCUMENT_TITLE)

    # Adding employee details
    employee = Employee.objects.get(id=employee_code)
    textLines = []
    textLines.append("EMPLOYEE DETAILS")
    textLines.append("   ")
    textLines.append(f"Employee Name : {employee.first_name} {employee.last_name}")
    textLines.append(f"Department    : {employee.department}")
    textLines.append(f"Role          : {employee.role}")
    textLines.append("   ")
    textLines.append("   ")

    # Add Myers Brigs result
    mbti_obj = EmployeeMBTI.objects.get(employee=employee)
    textLines.append(f"What is {employee.first_name}'s communication and interaction style?")
    textLines.append(f"Myers-Briggs Type:  {mbti_obj.mbti.type}")
    textLines.append(f"Summary: ")
    summary = mbti_obj.mbti.summary
    textLines.append("     ")
    li = summary.split()
    i = 0
    limit = 12
    while i<len(li):
        textLines.append(" ".join(li[i:i+limit]))
        i+=limit
    textLines.append("     ")

    # Working process summary
    ew_obj = EmployeeWorkingGenius.objects.get(employee=employee)
    textLines.append("     ")
    textLines.append("     ")
    textLines.append("WORKING PROCESS Summary:")
    textLines.append("     ")
    textLines.append("Geniuses:")
    textLines.append("     ")
    textLines.append(f"{ew_obj.wg_primary.input}   : {ew_obj.wg_primary.definition}")
    textLines.append(f"{ew_obj.wg_secondary.input} : {ew_obj.wg_secondary.definition}")
    textLines.append("     ")
    textLines.append("Competencies: ")
    textLines.append("     ")
    textLines.append(f"{ew_obj.wc_primary.input}   : {ew_obj.wc_primary.definition}")
    textLines.append(f"{ew_obj.wc_secondary.input} : {ew_obj.wc_secondary.definition}")
    textLines.append("     ")
    textLines.append("Frustrations: ")
    textLines.append("     ")
    textLines.append(f"{ew_obj.wf_primary.input}   : {ew_obj.wf_primary.definition}")
    textLines.append(f"{ew_obj.wf_secondary.input} : {ew_obj.wf_secondary.definition}")
    textLines.append("     ")

    text = canvas.beginText(40, 680)
    text.setFont(CANVAS_FONT, 14)

    for line in textLines:
        text.textLine(line)
    canvas.drawText(text)
    canvas.showPage()

    textLines = []
    
    # Add Temperament summary
    textLines.append("TEMPERAMENT Summary")
    textLines.append("     ")
    s_red =  EmployeeColourTraits.objects.filter(
        employee_id=employee, colour="RED", temparement__type="Sanguine"
        ).aggregate(Sum("score")).get("score__sum")
    s_green =  EmployeeColourTraits.objects.filter(
        employee_id=employee, colour="GREEN", temparement__type="Sanguine"
        ).aggregate(Sum("score")).get("score__sum")
    c_red =  EmployeeColourTraits.objects.filter(
        employee_id=employee, colour="RED", temparement__type="Choleric"
        ).aggregate(Sum("score")).get("score__sum")
    c_green =  EmployeeColourTraits.objects.filter(
        employee_id=employee, colour="GREEN", temparement__type="Choleric"
        ).aggregate(Sum("score")).get("score__sum")
    m_red =  EmployeeColourTraits.objects.filter(
        employee_id=employee, colour="RED", temparement__type="Melancholic"
        ).aggregate(Sum("score")).get("score__sum")
    m_green =  EmployeeColourTraits.objects.filter(
        employee_id=employee, colour="GREEN", temparement__type="Melancholic"
        ).aggregate(Sum("score")).get("score__sum")
    p_red =  EmployeeColourTraits.objects.filter(
        employee_id=employee, colour="RED", temparement__type="Phlegmatic"
        ).aggregate(Sum("score")).get("score__sum")
    p_green =  EmployeeColourTraits.objects.filter(
        employee_id=employee, colour="GREEN", temparement__type="Phlegmatic"
        ).aggregate(Sum("score")).get("score__sum")
    
    textLines.append("Sanguine")
    textLines.append("    ")
    textLines.append(f"Green Light Traits : {s_green}")
    textLines.append(f"Total Possible     : 75")
    textLines.append(f"Percentage         : {round((s_green/75)*100)}")
    textLines.append(f"Red Light Traits   : {s_red}")
    textLines.append(f"Total Possible     : 75")
    textLines.append(f"Percentage         : {round((s_red/75)*100)}")
    textLines.append("    ")


    textLines.append("Choleric")
    textLines.append("    ")
    textLines.append(f"Green Light Traits : {c_green}")
    textLines.append(f"Total Possible     : 85")
    textLines.append(f"Percentage         : {round((c_green/85)*100)}")
    textLines.append(f"Red Light Traits   : {c_red}")
    textLines.append(f"Total Possible     : 65")
    textLines.append(f"Percentage         : {round((c_red/65)*100)}")
    textLines.append("    ")


    textLines.append("Melancholic")
    textLines.append("    ")
    textLines.append(f"Green Light Traits : {m_green}")
    textLines.append(f"Total Possible     : 85")
    textLines.append(f"Percentage         : {round((m_green/85)*100)}")
    textLines.append(f"Red Light Traits   : {m_red}")
    textLines.append(f"Total Possible     : 65")
    textLines.append(f"Percentage         : {round((m_red/65)*100)}")
    textLines.append("    ")


    textLines.append("Phlygmatic")
    textLines.append("    ")
    textLines.append(f"Green Light Traits : {p_green}")
    textLines.append(f"Total Possible     : 85")
    textLines.append(f"Percentage         : {round((p_green/85)*100)}")
    textLines.append(f"Red Light Traits   : {p_red}")
    textLines.append(f"Total Possible     : 65")
    textLines.append(f"Percentage         : {round((p_red/65)*100)}")
    textLines.append("    ")

    text = canvas.beginText(40, 680)
    text.setFont(CANVAS_FONT, 14)

    for line in textLines:
        text.textLine(line)
    canvas.drawText(text)

    canvas.showPage()

    textLines = []

    # Skillset Summary
    textLines.append("SKILLSET Summary:")
    textLines.append("    ")

    tm_red = SKILL_CODES.get("TIME_MANAGEMENT").get("RED")
    tm_green = SKILL_CODES.get("TIME_MANAGEMENT").get("GREEN")
    ps_red = SKILL_CODES.get("PROBLEM_SOLVING").get("RED")
    ps_green = SKILL_CODES.get("PROBLEM_SOLVING").get("GREEN")
    cm_red = SKILL_CODES.get("CONFLICT_MANAGEMENT").get("RED")
    cm_green = SKILL_CODES.get("CONFLICT_MANAGEMENT").get("GREEN")
    pm_red = SKILL_CODES.get("PEOPLE_MANAGEMENT").get("RED")
    pm_green = SKILL_CODES.get("PEOPLE_MANAGEMENT").get("GREEN")
    oh_red = SKILL_CODES.get("OBJECTION_HANDLING").get("RED")
    oh_green = SKILL_CODES.get("OBJECTION_HANDLING").get("GREEN")
    
    tm_red_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=tm_red).aggregate(Sum("score")).get("score__sum")
    tm_green_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=tm_green).aggregate(Sum("score")).get("score__sum")
    ps_red_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=ps_red).aggregate(Sum("score")).get("score__sum")
    ps_green_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=ps_green).aggregate(Sum("score")).get("score__sum")
    cm_red_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=cm_red).aggregate(Sum("score")).get("score__sum")
    cm_green_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=cm_green).aggregate(Sum("score")).get("score__sum")
    pm_red_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=pm_red).aggregate(Sum("score")).get("score__sum")
    pm_green_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=pm_green).aggregate(Sum("score")).get("score__sum")
    oh_red_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=oh_red).aggregate(Sum("score")).get("score__sum")
    oh_green_value = EmployeeColourTraits.objects.filter(
        employee_id=employee, ctid_code__in=oh_green).aggregate(Sum("score")).get("score__sum")

    textLines.append(f"Time Management     : {get_skill_level(tm_red_value, tm_green_value)}")
    textLines.append(f"Problem Solving     : {get_skill_level(ps_red_value, ps_green_value)}")
    textLines.append(f"Conflict Management : {get_skill_level(cm_red_value, cm_green_value)}")
    textLines.append(f"People Management   : {get_skill_level(pm_red_value, pm_green_value)}")
    textLines.append(f"Objection Handling  : {get_skill_level(oh_red_value, oh_green_value)}")


    # Program Summary
    textLines.append("         ")
    textLines.append("PROGRAM Summary:")
    textLines.append("         ")
    textLines.append("Program   <-->  Level")
    textLines.append("         ")

    values = EmployeeProgramSkills.objects.filter(
        employee=employee).filter(level__gte=1).order_by("-level").values("program__program_name","level")
    
    for skills in values:
        textLines.append(f"{skills['program__program_name']}   <-->   {skills['level']}")

    text = canvas.beginText(40, 680)
    text.setFont(CANVAS_FONT, 14)

    for line in textLines:
        text.textLine(line)
    canvas.drawText(text)

    canvas.save()
    return canvas

