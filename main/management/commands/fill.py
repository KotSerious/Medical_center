from django.core.management import BaseCommand
from django.db import connection

from main.models import Doctor, LabTest


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Добавляем данные для модели Doctor
        doctors_data = [
            {
                'name': 'Доктор Иванов',
                'specialization': 'Кардиолог',
                'experience': 10,
                'description': 'Опытный кардиолог с 10-летним стажем работы.'
            },
            {
                'name': 'Доктор Петров',
                'specialization': 'Невролог',
                'experience': 8,
                'description': 'Специалист по неврологии с 8-летним опытом.'
            },
            # Добавьте других врачей по аналогии
        ]

        # Очистка таблицы Doctor
        Doctor.objects.all().delete()

        # Сброс автоинкремента для поля `pk` в таблице Doctor
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE main_doctor_id_seq RESTART WITH 1")

        # Список экземпляров класса Doctor
        doctor_create = []
        for doc_data in doctors_data:
            doctor_create.append(Doctor(**doc_data))

        # Добавление докторов в базу данных
        Doctor.objects.bulk_create(doctor_create)


        # Добавляем данные для модели LabTest
        lab_tests_data = [
            {
                'name': 'Анализ крови',
                'description': 'Общий анализ крови',
                'price': 1000,
                'time': 1
            },
            {
                'name': 'ЭКГ',
                'description': 'Электрокардиография',
                'price': 1500,
                'time': 2
            },
            # Добавьте другие лабораторные исследования по аналогии
        ]

        # Очистка таблицы LabTest
        LabTest.objects.all().delete()

        # Сброс автоинкремента для поля `pk` в таблице LabTest
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE main_labtest_id_seq RESTART WITH 1")

        # Список экземпляров класса Labtest
        labtest_create = []
        for lab_data in lab_tests_data:
            labtest_create.append(LabTest(**lab_data))

        # Добавление тесты в базу данных
        LabTest.objects.bulk_create(labtest_create)
