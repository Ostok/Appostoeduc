from django.shortcuts import render, redirect
from educ.forms import ContactoForm
from educ.forms import EstudianteForm
from educ.models import Estudiante, Eje



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
    
    
def contacto(request):
    contacto_form = ContactoForm()
    return render(request,'educ/publica/contacto.html',{'form': contacto_form})
    
    
def estudiante_nuevo(request):
    if request.method=='POST':
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            #nombre=formulario.cleaned_data['nombre']
            #apellido=formulario.cleaned_data['apellido']
            #email=formulario.cleaned_data['email']
            #dni=formulario.cleaned_data['dni']
            #nuevo=Estudiante(nombre=nombre,apellido=apellido,email=email,dni=dni)
            #nuevo.save()
            formulario.save()
            return redirect('estudiantes_index')
    else:
        formulario = EstudianteForm()
    return render(request,'educ/administracion/estudiantes/estudiante_nuevo.html',{'form': formulario})
    
    
def estudiantes_index(request):
    listado = Estudiante.objects.all()
    ejes = Eje.objects.all()
        
    return render(request,'educ/administracion/estudiantes/estudiantes_index.html',{
        'listado':listado,
        'ejes':ejes})
    
      
def estudiantes_editar(request, id_estudiante):
    try:
        estudiante = Estudiante.objects.get(pk=id_estudiante)
    except Estudiante.DoesNotExist():
        return HttpResponse("<h1>El id {{id_estudiante}} no existe")
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST, instance = estudiante)
        if formulario.is_valid():
            formulario.save()
            return redirect('estudiantes_index')
    else:
        formulario = EstudianteForm(instance = estudiante)
        return render(request,'educ/administracion/estudiantes/estudiantes_editar.html', {'form': formulario, 'estudiante': estudiante})


def estudiantes_borrar(request, id_estudiante):
    try:
        estudiante = Estudiante.objects.get(pk=id_estudiante)
    except Estudiante.DoesNotExist():
        return HttpResponse("<h1>El id {{id_estudiante}} no existe")
    estudiante.delete()
    return redirect('estudiantes_index')
