from django.shortcuts import render
from .models import Subject
from .forms import SubjectForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'attendance/index.html')

def homePage(request):
    print(request.user)
    if str(request.user)=='AnonymousUser':
        return HttpResponseRedirect('http://127.0.0.1:8000/accounts/login/')
    subjects=Subject.objects.filter(userid__exact=request.user)
    
    if request.method =='POST':
        form = SubjectForm(request.POST)
        instance=form.save(commit=False)
        instance.userid=request.user
        instance.save()
    form = SubjectForm()
    studentAttendance=[]
    for subject in subjects:
        studentAttendance.append(subject)
    
    context = {
        'studentAttendance': studentAttendance, 
        'form': form,
    }
    return render(request, 'attendance/home.html', context)

def deleteSub(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    return HttpResponseRedirect('http://127.0.0.1:8000/home/')


def updateAttendance(request, subject_id, attended):
    subject =Subject.objects.get(id=subject_id)
    if attended==0:
        subject.attended=subject.attended+1
        subject.total=subject.total+1
    else:
        subject.total=subject.total+1
    if subject.total!=0:
        subject.attendance='{0:.2f}'.format((subject.attended/subject.total)*100)

    subject.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/home/')


