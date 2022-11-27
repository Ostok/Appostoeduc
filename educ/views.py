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


def bio1eje1(request):
    lista_temas = [
        'caracterización de los seres vivos.',
        'concepto de sistema.',
        'niveles de organizacion de la materia.',
        'unidad y diversidad de funciones y estructuras.',
        'biodiversidad: aspectos evolutivos.',
        'arboles de parentezco entre los seres vivos.',
        'el origen de la vida.',
        'origen de células eucariotas. Teoría endosimbiótica.',
        'concepto general de célula procariota y eucariota.',
        'origen de la multicelularidad.',
        'la continuidad de la vida en las condiciones actuales: teoría celular.'
    ]
    return render(request,'educ/publica/bio1eje1.html',{'lista_temas': lista_temas})



def bio1eje2(request):
    return render(request,'educ/publica/bio1eje2.html')


def bio1eje3(request):
    return render(request,'educ/publica/bio1eje3.html')
