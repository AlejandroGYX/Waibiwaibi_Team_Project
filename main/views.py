
from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.forms import  UserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request): 
    return render(request, 'main/index.html')

def blog(request): 
    return render(request, 'main/blog.html')

def features(request): 
    return render(request, 'main/features.html')

def games(request): 
    return render(request, 'main/games.html')
@login_required
def contact(request): 
    return render(request, 'main/contact.html')

def single(request): 
    return render(request, 'main/single.html')

def single1(request): 
    return render(request, 'main/single1.html')

def single2(request): 
    return render(request, 'main/single2.html')


def action(request): 
    return render(request, 'main/action.html')


def others(request): 
    return render(request, 'main/others.html')

def racing(request): 
    return render(request, 'main/racing.html')

def rpg(request): 
    return render(request, 'main/rpg.html')

def rts(request): 
    return render(request, 'main/rts.html')

def shooting(request): 
    return render(request, 'main/shooting.html')

def sports(request): 
    return render(request, 'main/sports.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)


        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            

            
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
       
    
    return render(request, 'main/register.html', context={'user_form': user_form,  'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('main:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'main/login.html')



@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('main:index'))
 

