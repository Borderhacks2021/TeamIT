from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ("ACCOUNTING", "ACCOUNTING"),
        ("DEVELOPMENT", "DEVELOPMENT"),
        ("EXECUTIVE", "EXECUTIVE"),
        ("GOVERNMENT RELATIONS", "GOVERNMENT RELATIONS"),
        ("HUMAN RESOURCES", "HUMAN RESOURCES"),
        ("INVENTORY", "INVENTORY"),
        ("IT", "IT"),
        ("LEGAL", "LEGAL"),
        ("MANAGEMENT", "MANAGEMENT"),
        ("MARKETING", "MARKETING"),
        ("SALES", "SALES"),
        ("SERVICE", "SERVICE"),
        ("SUPPORT", "SUPPORT"),
    ]

    ROLE_CHOICES = [
        ("Front End Dev", "Front End Dev"),
        ("Back End Dev", "Back End Dev"),
        ("Full Stack Dev", "Full Stack Dev"),
        ("CEO","CEO"),
        ("CFO", "CFO"),
        ("COO", "COO"),
        ("CTO", "CTO"),
        ("Assisstant", "Assisstant"),
        ("Community Relations", "Community Relations"),
        ("Regulatory Admin", "Regulatory Admin"),
        ("Personnel and Benefits", "Personnel and Benefits"),
        ("Pay roll and AR/ AP", "Pay roll and AR/ AP"),
        ("Procurment and Logisitics Admin", "Procurment and Logisitics Admin"),
        ("Logisitics Assisstant", "Logisitics Assisstant"),
        ("Software Admin", "Software Admin"),
        ("Hardware Admin", "Hardware Admin"),
        ("Policy and Procedures", "Policy and Procedures"),
        ("Health and Safety", "Health and Safety"),
        ("Sales", "Sales"),
        ("Human Resources", "Human Resources"),
        ("Marketing", "Marketing"),
        ("Service", "Service"),
        ("Support", "Support"),
        ("Inventory", "Inventory"),
        ("Accounting", "Accounting"),
        ("Legal", "Legal"),
        ("Development", "Development"),
        ("IT", "IT"),
        ("Designer", "Designer"),
        ("Content Writer", "Content Writer"),
        ("Social Media", "Social Media"),
        ("Sr Sales Rep", "Sr Sales Rep"),
        ("Sales Rep", "Sales Rep"),
        ("Sr. Service Rep", "Sr. Service Rep"),
        ("Service Rep", "Service Rep"),
        ("Sr. Support Rep", "Sr. Support Rep"),
        ("Support Rep", "Support Rep")
    ]
    id = models.CharField(max_length=5, primary_key=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default="IT")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="IT")
    hourly_rate = models.FloatField()

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

