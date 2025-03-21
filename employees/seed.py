import os
import django
from django.conf import settings

# Настройка Django перед импортом моделей
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employeetree.settings')
django.setup()

import random
from datetime import datetime, timedelta
from employees.models import Department, Employee
from faker import Faker

fake = Faker()

def generate_departments():
    # Создаем корневое подразделение
    root = Department.objects.create(name="Компания")
    # Уровень 1 (5 подразделений)
    level1 = [Department.objects.create(name=f"Отдел {i}", parent=root) for i in range(1, 6)]
    # Уровень 2-5 (по 5 на каждом уровне)
    current_level = level1
    for _ in range(3):  # 3 дополнительных уровня
        next_level = []
        for dept in current_level:
            for i in range(1, 6):
                next_level.append(Department.objects.create(name=f"Подотдел {i}", parent=dept))
        current_level = next_level

def generate_employees():
    departments = Department.objects.all()
    for _ in range(50000):
        Employee.objects.create(
            full_name=fake.name(),
            position=fake.job(),
            hire_date=fake.date_between(start_date="-10y", end_date="today"),
            salary=random.uniform(30000, 150000),
            department=random.choice(departments)
        )

if __name__ == "__main__":
    generate_departments()
    print("Подразделения созданы")
    generate_employees()
    print("Сотрудники созданы")