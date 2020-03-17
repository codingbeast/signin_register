from django.shortcuts import render,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
# Create your views here.


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            try:
                next = request.GET['next']
            except:
                next="/sec"
            return redirect(next)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        myform = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.mob = form.cleaned_data.get('mob')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            try:
                next = request.GET['next']
            except:
                next="/sec"
            return redirect(next)
        else:
            form = SignUpForm()
            return render(request, 'accounts/signup.html', {'form': form,'myform': myform})
    else:
        #form = UserCreationForm()
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def index(request):
    myurl=reverse("sec")
    return render(request,"accounts/myindex.html",context={"myurl" : myurl})
@login_required(login_url='/login')
def sec(request):
    return render(request,"accounts/sec.html")

def Logout(request):
    logout(request)
    return render(request,"accounts/logout.html")
