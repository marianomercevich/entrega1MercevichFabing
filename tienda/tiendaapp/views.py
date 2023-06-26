from django.shortcuts import redirect, render
from django.http import HttpResponse
from pkg_resources import require
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required




def entrada (request):
    return redirect("index")

def index (request):
    return render (request, 'tiendaapp/index.html')


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request,"tiendaapp/index.html")
            else:
                return render(request,"tiendaapp/login.html")
        else:
            return render(request,"tiendaapp/login.html")
    
    form = AuthenticationForm()

    return render(request,"tiendaapp/login.html",{"form":form})

def register_request(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
       

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 

            form.save() 
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request,"tiendaapp/index.html")

            else:
                return render(request,"tiendaapp/register.html")


        return render(request,"tiendaapp/register.html",{"form":form})
    
    form = UserCreationForm()

    return render(request,"tiendaapp/register.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("index")

@login_required
def editar_perfil(request):

    user = request.user 

    if request.method == "POST":
        
        form = UserEditForm(request.POST) 

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.nick_name = info["nick_name"]
            # user.imagen = info["Imagen", required=False]

            user.save()

            return render(request,"tiendaapp/index.html",{"form":form})
    
    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})

    return render(request,"tiendaapp/editar_perfil.html", {"form":form})

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            # avatar.save()

            return render(request,"tiendaapp/index.html")

    else:
        form = AvatarForm()
    
    return render(request,"tiendaapp/agregar_avatar.html",{"form":form})


def contacto(request):

    return render (request, 'tiendaapp/contacto.html')

def nosotros(request):
    return render (request, 'tiendaapp/nosotros.html')


def Evento_view (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            Evento = evento.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(talle__icontains=search)| Q(precio__icontains=search) ).values()

            return render(request,"tiendaapp/Evento_view.html", {"Evento":Evento, "search":True, "busqueda":search})

    Evento = evento.objects.all()
    return render(request, 'tiendaapp/Evento_view.html', {"Evento":Evento, "search":False})

 

def Eventos (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            Evento = evento.objects.filter( 
                Q(Titulo__icontains=search) | 
                Q(Texto__icontains=search) | 
                Q(Fecha__icontains=search) | 
                Q(Estado__icontains=search) | 
                Q(Valor_de_la_entrada__icontains=search) | 
                Q(Pais__icontains=search) |                
                Q(Provincia__icontains=search) | 
                Q(Localidad__icontains=search) | 
                Q(Direccion__icontains=search) |
                Q(Organizador__icontains=search)|
                Q(imagen__icontains=search)
                ).values()
            return render(request,"tiendaapp/Eventos.html", {"Evento":Evento, "search":True, "busqueda":search})

    Evento = evento.objects.all()
    return render(request, "tiendaapp/Eventos.html", {"Evento":Evento, "search":False})

def crear_Evento (request):

    
    if request.method == "POST":

        formulario = EventoFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Evento = evento(
                Titulo=info["Titulo"], 
                Texto=info["Texto"], 
                Fecha=info["Fecha"], 
                Estado=info["Estado"], 
                Valor_de_la_entrada=info["Valor_de_la_entrada"], 
                Pais=info["Pais"], 
                Provincia=info["Provincia"], 
                Localidad=info["Localidad"], 
                Direccion=info["Direccion"], 
                Organizador=info["Organizador"],
                Imagen = info["imagen"]
                )

            Evento.save() 
            
            return redirect("Eventos")

        return render(request,"tiendaapp/formulario_evento.html",{"form":formulario})
    

    formulario = EventoFormulario()

    return render(request,"tiendaapp/formulario_evento.html",{"form":formulario})

def eliminar_Evento(request, Evento_id):

    Evento = evento.objects.get(id=Evento_id)
    Evento.delete()

    return redirect("Eventos")

def editar_Evento(request, Evento_id):

    event = evento.objects.get(id=Evento_id)

    if request.method == "POST":

        formulario = EventoFormulario(request.POST)

        if formulario.is_valid():

            info_Evento = formulario.cleaned_data
        
            event.Titulo = info_Evento["Titulo"]
            event.Texto = info_Evento["Texto"]
            event.Fecha = info_Evento["Fecha"]
            event.Estado = info_Evento ["Estado"]
            event.Valor_de_la_entrada = info_Evento["Valor_de_la_entrada"]
            event.Pais = info_Evento [" Pais "] 
            event.Provincia = info_Evento ["Provincia "] 
            event.Localidad = info_Evento ["Localidad "] 
            event.Direccion = info_Evento ["Direccion "] 
            event.Organizador = info_Evento ["Organizador "]
            event.imagen = info_Evento ["imagen"]
            event.save() # guardamos en la bd

            return redirect("Eventos")
   
    formulario = EventoFormulario(
        initial={
            "Titulo":event.Titulo,
            "Texto":event.Texto,
            "Fecha":event.Fecha,
            "Estado":event.Estado,
            "Valor_de_la_entrada":event.Valor_de_la_entrada,
            "Pais":event.Pais,
            "Provincia":event.Provincia,
            "Localidad":event.Localidad,
            "Direccion":event.Direccion,
            "Organizador":event.Organizador,
            "imagen":event.imagen
        }
    )
    
    return render(request,"tiendaapp/formulario_evento.html",{"form":formulario})


@login_required
def tienda (request):
    return render (request, 'tiendaapp/tienda.html')

def ver_producto(request):
   return render(request,"tiendaapp/ver_producto.html")

@login_required
def cascos (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            cascos = casco.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(talle__icontains=search)| Q(precio__icontains=search) ).values()

            return render(request,"tiendaapp/cascos.html", {"cascos":cascos, "search":True, "busqueda":search})

    cascos = casco.objects.all()
    return render(request, 'tiendaapp/cascos.html', {"cascos":cascos, "search":False})
  
def crear_casco(request):

    
    if request.method == "POST":

        formulario = CascoFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Casco = casco(marca=info["marca"], tipo=info["tipo"], talle=info["talle"], precio=info["precio"])
            Casco.save() 
            
            return redirect("cascos")

        return render(request,"tiendaapp/formulario_casco.html",{"form":formulario})
    

    formulario = CascoFormulario()
    
    return render(request,"tiendaapp/formulario_casco.html",{"form":formulario})

def eliminar_casco(request, casco_id):

    # post
    Casco = casco.objects.get(id=casco_id)
    Casco.delete()

    return redirect("cascos")

def editar_casco(request, casco_id):

    Casco = casco.objects.get(id=casco_id)

    if request.method == "POST":

        formulario = CascoFormulario(request.POST)

        if formulario.is_valid():

            info_casco = formulario.cleaned_data
        
            Casco.marca = info_casco["marca"]
            Casco.tipo = info_casco["tipo"]
            Casco.talle = info_casco["talle"]
            Casco.precio = info_casco["precio"]
            Casco.save() # guardamos en la bd

            return redirect("cascos")
   
    formulario = CascoFormulario(initial={"marca":Casco.marca,"tipo":Casco.tipo, "talle":Casco.talle, "precio":Casco.precio })
    return render(request,"tiendaapp/formulario_casco.html",{"form":formulario})

@login_required
def camperas (request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            camperas = campera.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(talle__icontains=search)| Q(precio__icontains=search) ).values()

            return render(request,"tiendaapp/camperas.html", {"camperas":camperas, "search":True, "busqueda":search})

    camperas = campera.objects.all()
    return render(request, 'tiendaapp/camperas.html', {"camperas":camperas, "search":False})

def crear_campera (request):

    
    if request.method == "POST":

        formulario = CamperaFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Campera = campera(marca=info["marca"], tipo=info["tipo"], talle=info["talle"], precio=info["precio"])
            Campera.save() 
            
            return redirect("camperas")

        return render(request,"tiendaapp/formulario_campera.html",{"form":formulario})
    

    formulario = CamperaFormulario()

    return render(request,"tiendaapp/formulario_campera.html",{"form":formulario})

def eliminar_campera(request, campera_id):

    # post
    Campera = campera.objects.get(id=campera_id)
    Campera.delete()

    return redirect("camperas")

def editar_campera(request, campera_id):

    Campera = campera.objects.get(id=campera_id)

    if request.method == "POST":

        formulario = CamperaFormulario(request.POST)

        if formulario.is_valid():

            info_campera = formulario.cleaned_data
        
            Campera.marca = info_campera["marca"]
            Campera.tipo = info_campera["tipo"]
            Campera.talle = info_campera["talle"]
            Campera.precio = info_campera["precio"]
            Campera.save() # guardamos en la bd

            return redirect("camperas")
   
    formulario = CamperaFormulario(initial={"marca":Campera.marca,"tipo":Campera.tipo, "talle":Campera.talle, "precio":Campera.precio })
    return render(request,"tiendaapp/formulario_campera.html",{"form":formulario})

@login_required
def guantes (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            guantes = guante.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(talle__icontains=search)| Q(precio__icontains=search) ).values()
            return render(request,"tiendaapp/guantes.html", {"guantes":guantes, "search":True, "busqueda":search})

    guantes = guante.objects.all()
    return render(request, 'tiendaapp/guantes.html', {"guantes":guantes, "search":False})
  
def crear_guante(request):

    
    if request.method == "POST":

        formulario = GuanteFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Guante = guante(marca=info["marca"], tipo=info["tipo"], talle=info["talle"], precio=info["precio"])
            Guante.save() # guardamos en la bd
            
            return redirect("guantes")
        return render(request,"tiendaapp/formulario_guante.html",{"form":formulario})
    
    formulario = GuanteFormulario()

    return render(request,"tiendaapp/formulario_guante.html",{"form":formulario})

def eliminar_guante(request, guante_id):

    # post
    Guante = guante.objects.get(id=guante_id)
    Guante.delete()

    return redirect("guantes")

def editar_guante(request, guante_id):

    Guante = guante.objects.get(id=guante_id)

    if request.method == "POST":

        formulario = GuanteFormulario(request.POST)

        if formulario.is_valid():

            info_guante = formulario.cleaned_data
        
            Guante.marca = info_guante["marca"]
            Guante.tipo = info_guante["tipo"]
            Guante.talle = info_guante["talle"]
            Guante.precio = info_guante["precio"]
            Guante.save() # guardamos en la bd

            return redirect("guantes")
   
    formulario = GuanteFormulario(initial={"marca":Guante.marca,"tipo":Guante.tipo, "talle":Guante.talle, "precio":Guante.precio })
    return render(request,"tiendaapp/formulario_guante.html",{"form":formulario})

@login_required
def equipajes (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            equipajes = equipaje.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(precio__icontains=search) ).values()
            return render(request,"tiendaapp/equipaje.html", {"equipajes":equipajes, "search":True, "busqueda":search})

    equipajes = equipaje.objects.all()
    return render(request, 'tiendaapp/equipaje.html', {"equipaje":equipajes, "search":False})
  
def crear_equipaje(request):

    
    if request.method == "POST":

        formulario = EquipajeFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Equipaje = equipaje(marca=info["marca"], tipo=info["tipo"], precio=info["precio"])
            Equipaje.save() # guardamos en la bd
            
            return redirect("equipaje")
        return render(request,"tiendaapp/formulario_equipaje.html",{"form":formulario})
    
    formulario = EquipajeFormulario()

    return render(request,"tiendaapp/formulario_equipaje.html",{"form":formulario})

def eliminar_equipaje(request, equipaje_id):

    # post
    Equipaje = equipaje.objects.get(id=equipaje_id)
    Equipaje.delete()

    return redirect("equipaje")

def editar_equipaje(request, equipaje_id):

    Equipaje = equipaje.objects.get(id=equipaje_id)

    if request.method == "POST":

        formulario = EquipajeFormulario(request.POST)

        if formulario.is_valid():

            info_equipaje = formulario.cleaned_data
        
            Equipaje.marca = info_equipaje["marca"]
            Equipaje.tipo = info_equipaje["tipo"]
            Equipaje.precio = info_equipaje["precio"]
            Equipaje.save() # guardamos en la bd

            return redirect("equipaje")
   
    formulario = EquipajeFormulario(initial={"marca":Equipaje.marca,"tipo":Equipaje.tipo, "precio":Equipaje.precio })
    return render(request,"tiendaapp/formulario_equipaje.html",{"form":formulario})

@login_required
def tecnologias (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            tecnologias = tecnologia.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(precio__icontains=search) ).values()
            return render(request,"tiendaapp/tecnologia.html", {"tecnologias":tecnologias, "search":True, "busqueda":search})

    tecnologias = tecnologia.objects.all()
    return render(request, 'tiendaapp/tecnologia.html', {"tecnologia":tecnologias, "search":False})
  
def crear_tecnologia(request):

    
    if request.method == "POST":

        formulario = TecnologiaFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Tecnologia = tecnologia(marca=info["marca"], tipo=info["tipo"], precio=info["precio"])
            Tecnologia.save() # guardamos en la bd
            
            return redirect("tecnologia")
        return render(request,"tiendaapp/formulario_tecnologia.html",{"form":formulario})
    
    formulario = TecnologiaFormulario()

    return render(request,"tiendaapp/formulario_tecnologia.html",{"form":formulario})

def eliminar_tecnologia(request, tecnologia_id):

    # post
    Tecnologia = tecnologia.objects.get(id=tecnologia_id)
    Tecnologia.delete()

    return redirect("tecnologia")

def editar_tecnologia(request, tecnologia_id):

    Tecnologia = tecnologia.objects.get(id=tecnologia_id)

    if request.method == "POST":

        formulario = TecnologiaFormulario(request.POST)

        if formulario.is_valid():

            info_tecnologia = formulario.cleaned_data
        
            Tecnologia.marca = info_tecnologia["marca"]
            Tecnologia.tipo = info_tecnologia["tipo"]
            Tecnologia.precio = info_tecnologia["precio"]
            Tecnologia.save() # guardamos en la bd

            return redirect("tecnologia")
   
    formulario = TecnologiaFormulario(initial={"marca":Tecnologia.marca,"tipo":Tecnologia.tipo, "precio":Tecnologia.precio })
    return render(request,"tiendaapp/formulario_tecnologia.html",{"form":formulario})

@login_required
def accesorios (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            accesorios = accesorio.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(precio__icontains=search) ).values()
            return render(request,"tiendaapp/accesorios.html", {"accesorios":accesorios, "search":True, "busqueda":search})

    accesorios = accesorio.objects.all()
    return render(request, 'tiendaapp/accesorios.html', {"accesorio":accesorios, "search":False})
  
def crear_accesorio(request):

    
    if request.method == "POST":

        formulario = AccesorioFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Accesorio = accesorio(marca=info["marca"], tipo=info["tipo"], precio=info["precio"])
            Accesorio.save() # guardamos en la bd
            
            return redirect("accesorios")
        return render(request,"tiendaapp/formulario_accesorio.html",{"form":formulario})
    
    formulario = AccesorioFormulario()

    return render(request,"tiendaapp/formulario_accesorio.html",{"form":formulario})

def eliminar_accesorio(request, accesorio_id):

    # post
    Accesorio = accesorio.objects.get(id=accesorio_id)
    Accesorio.delete()

    return redirect("accesorios")

def editar_accesorio(request, accesorio_id):

    Accesorio = accesorio.objects.get(id=accesorio_id)

    if request.method == "POST":

        formulario = AccesorioFormulario(request.POST)

        if formulario.is_valid():

            info_accesorio = formulario.cleaned_data
        
            Accesorio.marca = info_accesorio["marca"]
            Accesorio.tipo = info_accesorio["tipo"]
            Accesorio.precio = info_accesorio["precio"]
            Accesorio.save() # guardamos en la bd

            return redirect("accesorios")
   
    formulario = AccesorioFormulario(initial={"marca":Accesorio.marca,"tipo":Accesorio.tipo, "precio":Accesorio.precio })
    return render(request,"tiendaapp/formulario_accesorio.html",{"form":formulario})

@login_required
def repuestos (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            repuestos = repuesto.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(precio__icontains=search) ).values()
            return render(request,"tiendaapp/repuestos.html", {"repuestos":repuestos, "search":True, "busqueda":search})

    repuestos = repuesto.objects.all()
    return render(request, 'tiendaapp/repuestos.html', {"repuesto":repuestos, "search":False})
  
def crear_repuesto(request):

    
    if request.method == "POST":

        formulario = RepuestoFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Repuesto = repuesto(marca=info["marca"], tipo=info["tipo"], precio=info["precio"])
            Repuesto.save() # guardamos en la bd
            
            return redirect("repuestos")
        return render(request,"tiendaapp/formulario_repuesto.html",{"form":formulario})
    
    formulario = RepuestoFormulario()

    return render(request,"tiendaapp/formulario_repuesto.html",{"form":formulario})

def eliminar_repuesto(request, repuesto_id):

    # post
    Repuesto = repuesto.objects.get(id=repuesto_id)
    Repuesto.delete()

    return redirect("repuestos")

def editar_repuesto(request, repuesto_id):

    Repuesto = repuesto.objects.get(id=repuesto_id)

    if request.method == "POST":

        formulario = RepuestoFormulario(request.POST)

        if formulario.is_valid():

            info_repuesto = formulario.cleaned_data
        
            Repuesto.marca = info_repuesto["marca"]
            Repuesto.tipo = info_repuesto["tipo"]
            Repuesto.precio = info_repuesto["precio"]
            Repuesto.save() # guardamos en la bd

            return redirect("repuestos")
   
    formulario = RepuestoFormulario(initial={"marca":Repuesto.marca,"tipo":Repuesto.tipo, "precio":Repuesto.precio })
    return render(request,"tiendaapp/formulario_repuesto.html",{"form":formulario})

@login_required
def indumentarias (request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            indumentarias = indumentaria.objects.filter( Q(marca__icontains=search) | Q(tipo__icontains=search) | Q(talle__icontains=search)| Q(precio__icontains=search) ).values()
            return render(request,"tiendaapp/indumentaria.html", {"indumentaria":indumentarias, "search":True, "busqueda":search})

    indumentarias = indumentaria.objects.all()
    return render(request, 'tiendaapp/indumentaria.html', {"indumentaria":indumentarias, "search":False})
  
def crear_indumentaria(request):

    
    if request.method == "POST":

        formulario = IndumentariaFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data
        
            Indumentaria = indumentaria(marca=info["marca"], tipo=info["tipo"], talle=info["talle"], precio=info["precio"])
            Indumentaria.save() # guardamos en la bd
            
            return redirect("indumentaria")
        return render(request,"tiendaapp/formulario_indumentaria.html",{"form":formulario})
    
    formulario = IndumentariaFormulario()

    return render(request,"tiendaapp/formulario_indumentaria.html",{"form":formulario})

def eliminar_indumentaria(request, indumentaria_id):

    # post
    Indumentaria = indumentaria.objects.get(id=indumentaria_id)
    Indumentaria.delete()

    return redirect("indumentaria")

def editar_indumentaria(request, indumentaria_id):

    Indumentaria = indumentaria.objects.get(id=indumentaria_id)

    if request.method == "POST":

        formulario = IndumentariaFormulario(request.POST)

        if formulario.is_valid():

            info_indumentaria = formulario.cleaned_data
        
            Indumentaria.marca = info_indumentaria["marca"]
            Indumentaria.tipo = info_indumentaria["tipo"]
            Indumentaria.talle = info_indumentaria["talle"]
            Indumentaria.precio = info_indumentaria["precio"]
            Indumentaria.save() # guardamos en la bd

            return redirect("indumentaria")
   
    formulario = IndumentariaFormulario(initial={"marca":Indumentaria.marca,"tipo":Indumentaria.tipo, "talle":Indumentaria.talle, "precio":Indumentaria.precio })
    return render(request,"tiendaapp/formulario_indumentaria.html",{"form":formulario})

def en_construccion(request):
    return render(request,"tiendaapp/en_construccion.html")

def base(request):
    return render(request,"tiendaapp/base.html",{})

