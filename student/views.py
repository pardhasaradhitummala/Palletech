from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from student.forms import TraineeForm
from student.models import StudentModel


def getTraineeForm(request):
    context_email = ''
    form = TraineeForm()
    return render(request,'StudentRegistrationForm.html',{'form':form,'error':context_email})

def maketraineintodatabase(request):
    if request.method == 'POST':
        form = TraineeForm()
        email = request.POST['email']
        phone = request.POST['phone']
        objset = StudentModel.objects.filter(email=email)
        print(objset)
        if len(objset)>0:
            context_email = "Trainee already exists"
            return render(request, 'StudentRegistrationForm.html',{'form':form,'error':context_email})
        else:
            newform = TraineeForm()
            form = TraineeForm(request.POST,request.FILES)

            if form.is_valid():
                print('form is valid')
                form.save()
            context_email = ''
            return render(request, 'StudentRegistrationForm.html', {'form': newform, 'error': context_email})

def traineesearch(request):
    return render(request,'traineesearch.html',{'msg':''})

def searchingtrainee(request):
    if request.method == 'POST':
        email = request.POST['email']
        objset = StudentModel.objects.filter(email=email)
        globals()['obj'] = objset
        if len(objset) == 0:
            return render(request,'traineesearch.html',{'msg':'Record not found'})
        else:
            data = objset[0]
            return render(request,'studentrecord.html',{'data':data})



