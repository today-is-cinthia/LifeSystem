from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['contraseña']

        

        print(username,password)
        return redirect('dashboard')
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')