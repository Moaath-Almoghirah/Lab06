from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    context = {'students': students, 'form': form}
    return render(request, 'students.html', context)

def courses(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    context = {'courses': courses, 'form': form}
    return render(request, 'courses.html', context)

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    available_courses = Course.objects.exclude(students=student)
    
    if request.method == 'POST':
        course_name = request.POST.get('course')
        if course_name:
            course = Course.objects.get(name=course_name)
            student.courses.add(course)
            student.save()
            return redirect('details', student_id=student_id)

    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})