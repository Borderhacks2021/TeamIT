from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from report.utilities import generate_report


@csrf_exempt
def prepareReport(request):
    if request.method == "POST":
        emp_code = request.POST.get("emp_code")
        filename = "employee_report.pdf"
        f = open(filename, 'rb')
        pdf_contents = f.read()
        f.close()
        generate_report(emp_code)
        response = HttpResponse(pdf_contents, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        return response
    else:
        return render(request, 'index.html', {})
