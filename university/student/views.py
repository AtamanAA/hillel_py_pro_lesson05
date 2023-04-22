import random

from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from faker import Faker

from .models import Student


def index(request):
    return HttpResponse("Students index page.")


def generate_student(request):
    fake = Faker()
    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=random.randint(16, 60))
    return HttpResponse(f"Generate one fake student: {student}")


def generate_students(request):
    try:
        if request.GET["count"].isdigit() and 0 < int(request.GET["count"]) <= 100:
            count = int(request.GET["count"])
            fake = Faker()
            students_list = []
            for _ in range(count):
                students_list.append(Student(first_name=fake.first_name(),
                                             last_name=fake.last_name(),
                                             age=random.randint(16, 60)))
            students = Student.objects.bulk_create(students_list)
            return HttpResponse(f"Generate {count} fake students: <p>{students}</p>")
        else:
            count = request.GET["count"]
            return HttpResponse(f"Count {count} is not valid! Try again")
    except MultiValueDictKeyError:
        return HttpResponse('Query parameter "count" did not find! Try again')
