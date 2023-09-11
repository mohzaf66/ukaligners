from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Patient,User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_superuser:    
        totalpatientscount=Patient.objects.count()
        acceptedpatientscount=Patient.objects.filter(Status="Accept").count()
        reviewpatientscount=Patient.objects.filter(Status="Review").count()
        declinedpatientscount=Patient.objects.filter(Status="Decline").count()
    else:
        totalpatientscount=Patient.objects.filter(Dentist=request.user).count()
        acceptedpatientscount=Patient.objects.filter(Dentist=request.user,Status="Accept").count()
        reviewpatientscount=Patient.objects.filter(Dentist=request.user,Status="Review").count()
        declinedpatientscount=Patient.objects.filter(Dentist=request.user,Status="Decline").count()
    context={
        'dashboard':'active',
        'totalpatientscount':totalpatientscount,
        'acceptedpatientscount':acceptedpatientscount,
        'reviewpatientscount':reviewpatientscount,
        'declinedpatientscount':declinedpatientscount,

    }
    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def patients(request):
    if request.user.is_superuser:
        mypatients=Patient.objects.order_by("-id")
    else:
        mypatients=Patient.objects.filter(Dentist=request.user).order_by("-id")
    context={
        'patients':'active',
        'mypatients':mypatients,
    }

    return render(request,'patients.html',context)

@login_required(login_url='login')
def patientaccepted(request):
    if request.user.is_superuser:
        mypatients=Patient.objects.order_by("-id")
    else:    
        mypatients=Patient.objects.filter(Dentist=request.user,Status="Accept").order_by("-id")
    context={
        'patients':'active',
        'mypatients':mypatients,
    }

    return render(request,'patientaccepted.html',context)

@login_required(login_url='login')
def patientreview(request):
    if request.user.is_superuser:
        mypatients=Patient.objects.order_by("-id")
    else:    
        mypatients=Patient.objects.filter(Dentist=request.user,Status="Review").order_by("-id")
    context={
        'patients':'active',
        'mypatients':mypatients,
    }

    return render(request,'patientreview.html',context)

@login_required(login_url='login')
def patientdeclined(request):
    if request.user.is_superuser:
        mypatients=Patient.objects.order_by("-id")
    else:    
        mypatients=Patient.objects.filter(Dentist=request.user,Status="Decline").order_by("-id")
    context={
        'patients':'active',
        'mypatients':mypatients,
    }

    return render(request,'patientdeclined.html',context)

@login_required(login_url='login')
def dentists(request):
    dentists=User.objects.order_by("id")
    context={
        'dentists':'active',
        'dentists':dentists,
    }
    return render(request,'dentists.html',context)

@login_required(login_url='login')
def addnewpatient(request):
    if request.method=="POST":
        Dentist=request.user
        PatientName=request.POST.get('PatientName')
        PatientID=request.POST.get('PatientID')
        Clinic=request.POST.get('Clinic')
        Prescriber=request.POST.get('Prescriber')
        Invoice=request.POST.get('Invoice')
        Balance_To_Pay=request.POST.get('BalanceToPay')
        Surgery=request.POST.get('Surgery')
        Fee=request.POST.get('Fee')
        Status=request.POST.get('Status')
        Note=request.POST.get('Note')
        patient=Patient(Dentist=Dentist,PatientName=PatientName,PatientID=PatientID,Clinic=Clinic,Prescriber=Prescriber,Invoice=Invoice,Balance_To_Pay=Balance_To_Pay,Surgery=Surgery,Fee=Fee,Status=Status,Note=Note)
        patient.save()
        messages.success(request,"Patient added successfully!")

    context={
        'dentists':'active'
    }
    return render(request,'addnewpatient.html',context)

def patientdetail(request,id):
    patient=Patient.objects.get(id=id)
    context={
        'patient':patient,
    }
    return render(request, 'patientdetail.html', context)

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else: 
        if request.method=='POST':
            username= request.POST.get('username')
            password= request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Incorrect Username or Password is.Please try!")
        context={
            
        }
        return render(request,'login.html',context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:    
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get("username")
                messages.error(request,"Registration Successful")
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'signup.html',context)    

def logoutuser(request):
    logout(request)
    return redirect('login')

    return render(request,'login.html',context)