from django.urls import path

from report.views import prepareReport

app_name = 'report'

urlpatterns = [
        path("", prepareReport),
    ]