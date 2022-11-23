from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'educ/publica/index.html')
    
def bio1(request):
    return render(request,'educ/publica/bio1.html')
    
def bio2(request):
    return render(request,'educ/publica/bio3.html')
    
def bio3(request):
    return render(request,'educ/publica/bio3.html')
    
def eco4(request):
    return render(request,'educ/publica/eco4.html')
