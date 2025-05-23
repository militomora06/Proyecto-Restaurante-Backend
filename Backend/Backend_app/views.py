from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def registro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        email = data.get('email')
        contraseña = data.get('contraseña')

        if User.objects.filter(username=email).exists():
            return JsonResponse({'mensaje': 'El email ya está registrado'}, status=400)

        user = User.objects.create_user(username=email, first_name=nombre, email=email, password=contraseña)
        return JsonResponse({'mensaje': 'Usuario registrado correctamente'})

@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        contraseña = data.get('contraseña')

        user = authenticate(username=email, password=contraseña)

        if user is not None:
            login(request, user)
            return JsonResponse({'mensaje': 'Login exitoso', 'usuario': user.first_name})
        else:
            return JsonResponse({'mensaje': 'Credenciales inválidas'}, status=401)
