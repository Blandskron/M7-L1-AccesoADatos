from django.shortcuts import render
from django.db import connection
from .models import Student

def custom_sql_query(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM school_student WHERE age > %s", [18])
        rows = cursor.fetchall()

    return render(request, 'students.html', {'students': rows})

def raw_query_example(request):
    students = Student.objects.raw('SELECT * FROM school_student WHERE age < %s', [18])
    return render(request, 'students.html', {'students': students})
