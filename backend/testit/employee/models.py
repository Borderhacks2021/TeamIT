from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model
from datastore.models import Program, MBTISummary, TemparementSummary, WorkingGenius

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

class EmployeeProgramSkills(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])

    def __str__(self):
        return f"{self.employee.id} - {self.program.program_name} - {self.level}"  


class EmployeeMBTI(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    mbti = models.ForeignKey(MBTISummary, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.id} - {self.mbti.type}"

class EmployeeWorkingGenius(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    wg_primary = models.ForeignKey(WorkingGenius, on_delete=models.CASCADE, related_name="wg_primary")
    wg_secondary = models.ForeignKey(WorkingGenius, on_delete=models.CASCADE, related_name="wg_secondary")
    wc_primary = models.ForeignKey(WorkingGenius, on_delete=models.CASCADE, related_name="wc_primary")
    wc_secondary = models.ForeignKey(WorkingGenius, on_delete=models.CASCADE, related_name="wc_secondary")
    wf_primary = models.ForeignKey(WorkingGenius, on_delete=models.CASCADE, related_name="wf_primary")
    wf_secondary = models.ForeignKey(WorkingGenius, on_delete=models.CASCADE, related_name="wf_secondary")

    def __str__(self):
        return f"{self.employee.id}"

class EmployeeColourTraits(models.Model):
    COLOUR_CHOICES = [
        ("RED", "RED"),
        ("GREEN", "GREEN"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    ctid_code = models.CharField(max_length=20)
    temparement = models.ForeignKey(TemparementSummary, on_delete=models.CASCADE)
    trait = models.CharField(max_length=100)
    score = models.PositiveBigIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    colour = models.CharField(max_length=10, choices=COLOUR_CHOICES, default="RED")

    def __str__(self):
        return f"{self.employee.id} - {self.ctid_code} - {self.score}"