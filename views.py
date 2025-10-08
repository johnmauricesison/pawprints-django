from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.core.exceptions import ObjectDoesNotExist

from .models import AnimalReport
from .forms import AnimalReportForm

from .models import UserProfile
from .forms import ProfileForm

from .models import Event
from .forms import EventsForm

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        profile = UserProfile(user=myuser, fname=fname, lname=lname, email=email)
        profile.save()

        messages.success(request, "Your account has been successfully created.")
        return redirect('mylogin')
    
    return render(request, "myapp/signin.html")

def mylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return render(request,'myapp/lostpets.html', {'fname':user.first_name})
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('mylogin') 
    else:  
        return render(request, "myapp/login.html")

def logouts(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('land')

def cases(request):
    form = AnimalReportForm()
    if request.method == 'POST':
        form = AnimalReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal Report submitted successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, "Error, Please try again")
    
    context = {
        'form' : form
    }
    return render(request, 'myapp/cases.html', context)

def dashboard(request):

    user_profiles = UserProfile.objects.all()
    context = {
        'user_profiles': user_profiles
    }

    return render(request, "myapp/dashboard.html", context)

def about(request):
    return render(request, "myapp/about.html")

def profile(request):
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user = request.user)
        except ObjectDoesNotExist:
            return redirect('signin')
        
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = ProfileForm(instance=profile)
        
        context = {
            'form' : form,
            'profile' : profile
        }
        return render(request, "myapp/profile.html", context)
    else:
        return redirect('signin')

def lostpets(request):

    lostfound = AnimalReport.objects.filter(report_type__in=['LOST', 'FOUND'])

    if request.method == 'GET':
        query = request.GET.get('q')
        animaltype = request.GET.get('animal-type')
        colors = request.GET.get('color')
        sizes = request.GET.get('size')

        if query:
            lostfound = lostfound.filter(name__icontains=query)
        if animaltype:
            lostfound = lostfound.filter(animal_type = animaltype)
        if colors:
            lostfound = lostfound.filter(color = colors)
        if sizes:
            lostfound = lostfound.filter(size = sizes)
        
    context = {
        'lostfound':lostfound
    }

    return render(request, "myapp/lostpets.html", context)

def adoption(request):
    adopt = AnimalReport.objects.filter(report_type__in=['ADOPT'])

    if request.method == 'GET':
        query = request.GET.get('q')
        animaltype = request.GET.get('animal-type')
        colors = request.GET.get('color')
        sizes = request.GET.get('size')

        if query:
            adopt = adopt.filter(name__icontains=query)
        if animaltype:
            adopt = adopt.filter(animal_type = animaltype)
        if colors:
            adopt = adopt.filter(color = colors)
        if sizes:
            adopt = adopt.filter(size = sizes)
        
    context = {
        'adopt':adopt
    }
    return render(request, "myapp/adoption.html", context)

def events(request):

    events = Event.objects.all()

    context = {
        'events': events
    }
    return render(request, "myapp/events.html", context)

def wset(request):
    return render(request, "myapp/wset.html")

def land(request):
    return render(request, "myapp/land.html")

def base(request):
    return render(request, "myapp/base.html")
