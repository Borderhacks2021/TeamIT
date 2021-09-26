from django.urls import path

from report.views import prepareReport, homepage

app_name = 'report'

urlpatterns = [
        path("", homepage),
        path("reports/", prepareReport),
    ]