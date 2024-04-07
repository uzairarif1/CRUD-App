from django.shortcuts import get_object_or_404, render,redirect
from .forms import SignupForm,LoginForm,AddStudentForm,UpdateStudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .models import Record
from django.http import JsonResponse


# Create your views here.

#Homepage
def index(request):
    return render(request,'student/index.html')

def signup(request):
    
    if request.method == 'POST':
        regform = SignupForm(request.POST)
        if regform.is_valid():
            regform.save()
            redirect('')
    else:
        regform = SignupForm()

    return render (request,'student/signup.html',{
        'form':regform,
    })

def login(request):

    if request.method =='POST':
        loginform = LoginForm(request, data = request.POST)
        if loginform.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            
    else:
        loginform= LoginForm()

    return render(request,'student/login.html',{
        'form':loginform
    })

@login_required
def dashboard(request):
    record = Record.objects.all()
    return render(request,'student/dashboard.html',{
        'records':record
    })
@login_required
def add_student(request):

    if request.method=='POST':

        add_form = AddStudentForm(request.POST)
        if add_form.is_valid:
            add_form.save()
            return redirect('dashboard')
    else:
        add_form=AddStudentForm()

    return render(request,'student/add_student.html',{
        'form':add_form
    })


@login_required
def update_student(request,pk):
    record = Record.objects.get(id=pk)
    
    if request.method=='POST':
        form = UpdateStudentForm(request.POST,instance = record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form=UpdateStudentForm(instance=record)

    return render(request,'student/update_student.html',{
        'form':form
    })

@login_required
def view_student(request,pk):

    info=Record.objects.get(id=pk)

    return render(request,'student/view_student.html',{
        'info': info
    })

@login_required
def delete_student(request,pk):
    info=Record.objects.get(id=pk)
    info.delete()
    return redirect('dashboard')

# @login_required
# def delete_student(request, pk):
#     if request.method == 'POST' and request.is_ajax():
#         info = get_object_or_404(Record, id=pk)
#         info.delete()
#         return JsonResponse({'status': 'success', 'message': 'Student deleted successfully'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required
def signout(request):
    auth.logout(request)
    return redirect('login')