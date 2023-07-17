from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['contraseña']

        print(username,password)
    return render(request, 'index.html')