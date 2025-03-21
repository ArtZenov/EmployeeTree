from django.core.management.base import BaseCommand
from employees.models import Department, Employee
import random
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with departments and employees'

    def handle(self, *args, **options):
        self.stdout.write("Создание подразделений...")
        root = Department.objects.create(name="Компания")
        level1 = [Department.objects.create(name=f"Отдел {i}", parent=root) for i in range(1, 6)]
        current_level = level1
        for _ in range(3):
            next_level = []
            for dept in current_level:
                for i in range(1, 6):
                    next_level.append(Department.objects.create(name=f"Подотдел {i}", parent=dept))
            current_level = next_level
        self.stdout.write("Подразделения созданы")

        self.stdout.write("Создание сотрудников...")
        departments = Department.objects.all()
        for _ in range(50000):
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_between(start_date="-10y", end_date="today"),
                salary=random.uniform(30000, 150000),
                department=random.choice(departments)
            )
        self.stdout.write("Сотрудники созданы")
