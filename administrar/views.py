from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrar.models import Tarea # Importar el modelo
from .forms import TareaForm

# Create your views here.
def v_index(request):
  if request.method == 'POST':
    ######
    # Post, voy a crear un registro
    ######
    _titulo = request.POST["titulo"]

    datos = request.POST.copy()

    form =TareaForm(datos) # Para validaciones
    if form.is_valid():
      # validaciones extras usando el leenguaje python
      #si es valido guardo los datos
      form.save() # En este punto guardo en la base de datos
    else:
      #formulario tiene errores
      return HttpResponseRedirect("/")

    if False:
      #solo en el caso de que se desee guardar datos sin validaciones
    
      tarea = Tarea() # Instancio un modelo
      tarea.titulo = _titulo # Asigno titulo a la tarea
    
    # Antes de *.save, no se guarda nada en en DB
      tarea.save() # Guardo de base de datos
    
    return HttpResponseRedirect("/")
  else:
    #Peticiones method = GET
    consulta = Tarea.objects.filter(titulo__icontains = request.GET.get("titulo", ""))
    if request.GET.get("estado", "") != "":
      consulta = consulta.filter(estado = request.GET.get("estado", ""))
    
    ## Listar las tareas
    context = {
      'var1': 'Valor1',
      'var2': 'Valorasdasdasdasdasd',
      'lista': consulta
    }
    return render(request, 'pagina_x.html', context)

def v_eliminar(request, tarea_id):
  Tarea.objects.filter(id = tarea_id).delete()
  return HttpResponseRedirect("/") # Redirigir

def v_completado(request, tarea_id):
  task = Tarea.objects.get(id = tarea_id)
  task.estado = 1
  task.save()
  return HttpResponseRedirect('/')