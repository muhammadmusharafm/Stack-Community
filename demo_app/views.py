from django.shortcuts import render

from demo_app.forms import officerform,farmerform


# Create your views here.
def home(request):
     return render(request,'today.html')

def newindex(request):
         return render(request,'newindex.html')

def index(request):
         return render(request,'index.html')

def today2(request):
         return render(request,'today2.html')

def admin_dashboard(request):
         return render(request, 'admin_dashboard.html')

def login_view(request):
         return render(request, 'login.html')

def hello_view(request):
    return render(request,'hello.html')

def officer_reg(request):
    form=officerform()
    if request.method=='POST':
        form=officerform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_officerform=True
            user.save()
    return render(request,'officer_reg.html',{'form':form})

def farmer_reg(request):
    form=farmerform()
    if request.method=='POST':
        form=farmerform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_farmer=True
            user.save()
    return render(request,'farmer_reg.html',{'form':form})


