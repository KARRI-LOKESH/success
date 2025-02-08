from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status
from stdapp.models import Student 
from django.template import loader
from django.shortcuts import redirect
from .forms import StudentForm 
from django.contrib import messages

def display(request):
    s1 = '<h1>helloworld</h1>'
    return HttpResponse(s1)

@api_view(['GET'])
def StudentList(request):
    student_obj = Student.objects.all()
    serializer_obj = StudentSerializer(student_obj, many=True)
    return Response({'status_code': 200, 'status': 'OK', 'data': serializer_obj.data})

class StudentListData(APIView):
    def get(self, request, sid=None):
        student_obj = Student.objects.get(id=sid)
        serializer_obj = StudentSerializer(student_obj)
        return Response({'status_code': 200, 'status': 'OK', 'data': serializer_obj.data})

class StudentData(APIView):
    serializer_class = StudentSerializer

    def post(self, request):
        try:
            student_serializer = self.serializer_class(data=request.data, context={'request': request})
            student_serializer.is_valid(raise_exception=True)
            status_code = status.HTTP_200_OK
            response = {'status': 'success', 'status': status_code, 'message': "successfully posted", 'student_details': student_serializer.data}
        except Exception as error:
            status_code = status.HTTP_500_INTERNAL_SERVER
            response = {'status': 'failure', 'status': status_code, 'message': "retry", 'error': str(error)}
        return Response(response, status=status_code)

def members(request):
    mydata = Student.objects.all()
    temp = loader.get_template('all_members.html')
    context = {'mydata': mydata}
    return HttpResponse(temp.render(context, request))

def student_signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rollno = form.cleaned_data['rollno']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            student = Student(
                name=name,
                rollno=rollno,
                age=age,
                email=email,
                phone=phone
            )
            student.save()

            messages.success(request, 'Student data has been saved successfully!')
            return redirect('student_signup')  # Redirect to the signup page or another page
        else:
            messages.error(request, 'There was an error with your signup form.')

    else:
        form = StudentForm()

    return render(request, 'student_signup.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        rollno = request.POST.get('rollno')
        email = request.POST.get('email')

        # Check if student exists
        try:
            student = Student.objects.get(rollno=rollno, email=email)
            messages.success(request, f'Welcome, {student.name}!')
            return redirect('http://localhost:3000/')  # Redirect to home or another page
        except Student.DoesNotExist:
            messages.error(request, 'Invalid roll number or email.')

    return render(request, 'student_login.html')