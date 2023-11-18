from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Events
from .forms import Event
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate  # add to imports
from .forms import LoginForm
# Create your views here.
def home(request):
    context = {}
    context["dataset"]= Events.objects.all()
    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST' :
        Task = Event(request.POST, request.FILES)
        if Task.is_valid():
            Task.save()
            return redirect('/')
    else:
        Task = Event()
        return render(request,'create.html',{'form':Task})

def detail_view(request,id):
    context={}
    context["data"] = Events.objects.get(id= id)
    return render(request,'detail.html',context)

def register_event(request, id):
    event = get_object_or_404(Events, pk=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            # Optionally, you can perform additional actions like sending a confirmation email
            return render(request, 'success.html')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, 'event': event})

def login_view(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Login Failed! Invalid username or passwaord")
    return render(request, 'login.html', {'form': form})