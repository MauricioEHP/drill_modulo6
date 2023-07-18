from django.shortcuts import render
from django.contrib import messages
from .forms import VehiculoForm, RegistroUsuarioForm, RegistroUsuarioForm2
from django.http import HttpResponse, HttpResponseRedirect
from tokenize import PseudoExtras
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from .models import VehiculoModel
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.


def indexView(request):
    template_name = 'index.html'
    return render(request, template_name)





def agregarView(request):
    
    form =VehiculoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = VehiculoForm()
        messages.success(request, 'Vehiculo agregado correctamente')

    return render(request, "agregar.html", {'form': form})

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            #content_type = ContentType.objects.get_for_model(VehiculoModel)
            #visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)

            user = form.save()

            grupo = Group.objects.get(name='Gvisualizar')
            user.groups.add(grupo)
            login(request, user)
            messages.success(request, "¡¡Registrado con exito!!")
            return HttpResponseRedirect('/')
        messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
    form = RegistroUsuarioForm()
    context = {"register_form": form }
    return render(request, "registro.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Sesión iniciada como {username}.")
                return HttpResponseRedirect('/vehiculo/')
            else:
                messages.error(request, "¡¡Usuario o  password erroneo!!")
        else:
            messages.error(request, "¡¡Usuario o password erroneo!!")

    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/vehiculo/')

def listar_vehiculo(request):
    vehiculos = VehiculoModel.objects.all()
    context = {'lista_vehiculos': vehiculos}
    return render(request, 'lista.html', context)

def registro_view2(request):
    if request.method == "POST":
        form = RegistroUsuarioForm2(request.POST)
        if form.is_valid():
       
           username = form.cleaned_data['username']
           email = form.cleaned_data['email']
           password = form.cleaned_data['password']
           tipo_usuario = form.cleaned_data['tipo_usuario']

           user = User.objects.create_user(username=username, email=email, password=password)
           user.save()
            
           grupo = None  # Inicializar la variable grupo

           if tipo_usuario == 'Gvisualizar':
                grupo = Group.objects.get(name='Gvisualizar')
           elif tipo_usuario == 'ver_addgrupo':
                grupo = Group.objects.get(name='ver_addgrupo')
           elif tipo_usuario == 'staff':
                user.is_staff = True  # Si el rol seleccionado es 'staff', marcar al usuario como staff

           if grupo is not None:
                user.groups.add(grupo)
                

            

           login(request, user)
           messages.success(request, "¡Registrado con éxito!")
           return HttpResponseRedirect('/')
        
        messages.error(request, "Registro inválido. Algunos datos ingresados no son correctos")
    
    form = RegistroUsuarioForm2()
    context = {"register_form": form}
    return render(request, "registro2.html", context)

class MenuPermissionsMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return (
            user.groups.filter(name='ver_addgrupo').exists() or
            user.groups.filter(name='Gvisualizar').exists() or
            user.is_staff
        )