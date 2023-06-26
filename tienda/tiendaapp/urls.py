from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name = 'index'), 

    path('login', login_request, name = 'login'), 
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path('agregar_avatar', agregar_avatar, name="agregar_avatar"),

    path ('nosotros/', nosotros, name = 'nosotros'),  
    path ('contacto/', contacto, name = 'contacto'),  
 
    path ('tienda/', tienda, name = 'tienda'),
    path ('ver_producto', ver_producto, name = 'ver_producto'),

    path('cascos/', cascos, name = 'cascos'),
    path('crear_casco/', crear_casco, name="crear_casco"),
    path('eliminar_casco/<casco_id>/', eliminar_casco, name="eliminar_casco"),
    path('editar_casco/<casco_id>/', editar_casco, name="editar_casco"),

    path('camperas/', camperas, name = 'camperas'),
    path('crear_campera/', crear_campera, name="crear_campera"),
    path('eliminar_campera/<campera_id>/', eliminar_campera, name="eliminar_campera"),
    path('editar_campera/<campera_id>/', editar_campera, name="editar_campera"),

    path('guantes/', guantes, name = 'guantes'),
    path('crear_guante/', crear_guante, name="crear_guante"),
    path('eliminar_guante/<guante_id>/', eliminar_guante, name="eliminar_guante"),
    path('editar_guante/<guante_id>/', editar_guante, name="editar_guante"),

    path('indumentaria/', indumentarias, name = 'indumentaria'),
    path('crear_indumentaria/', crear_indumentaria, name="crear_indumentaria"),
    path('eliminar_indumentaria/<indumentaria_id>/', eliminar_indumentaria, name="eliminar_indumentaria"),
    path('editar_indumentaria/<indumentaria_id>/', editar_indumentaria, name="editar_indumentaria"),

    path('accesorios/', accesorios, name = 'accesorios'),
    path('crear_accesorio/', crear_accesorio, name="crear_accesorio"),
    path('eliminar_accesorio/<accesorio_id>/', eliminar_accesorio, name="eliminar_accesorio"),
    path('editar_accesorio/<accesorio_id>/', editar_accesorio, name="editar_accesorio"),
    
    path('equipaje/', equipajes, name = 'equipaje'),
    path('eliminar_equipaje/<equipaje_id>/', eliminar_equipaje, name="eliminar_equipaje"),
    path('crear_equipaje/', crear_equipaje, name="crear_equipaje"),
    path('editar_equipaje/<equipaje_id>/', editar_equipaje, name="editar_equipaje"),

    path('repuestos/', repuestos, name = 'repuestos'),
    path('eliminar_repuesto/<repuesto_id>/', eliminar_repuesto, name="eliminar_repuesto"),
    path('crear_repuesto/', crear_repuesto, name="crear_repuesto"),
    path('editar_repuesto/<repuesto_id>/', editar_repuesto, name="editar_repuesto"),

    path('tecnologia/', tecnologias, name = 'tecnologia'),
    path('eliminar_tecnologia/<tecnologia_id>/', eliminar_tecnologia, name="eliminar_tecnologia"),
    path('crear_tecnologia/', crear_tecnologia, name="crear_tecnologia"),
    path('editar_tecnologia/<tecnologia_id>/', editar_tecnologia, name="editar_tecnologia"),
        
    path('Eventos/', Eventos, name = 'Eventos'),
    path('eliminar_Evento/<Evento_id>/', eliminar_Evento, name="eliminar_Evento"),
    path('crear_Evento/', crear_Evento, name="crear_Evento"),
    path('editar_Evento/<Evento_id>/', editar_Evento, name="editar_Evento"),
    
    path('Evento_view/', Evento_view, name= "Evento_view" ),
    path('en_construccion/', en_construccion, name= "en_construccion" )
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)