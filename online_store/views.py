from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from .forms import Registration
from django.db import IntegrityError


def index(request):
    return render(request, 'online_store/index.html')

def register(request):
    form = Registration
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        password_again = request.POST['password_again']
        email = request.POST['email']
        if not password:
            return render(request, 'registration/register.html', {'form': form, 'message': 'password can not be empty'})
        if password != password_again:
            return render(request, 'registration/register.html', {'form': form, 'message': 'passwords do not mach'})
        if not email:
            return render(request, 'registration/register.html', {'form': form, 'message': 'email not be empty'})
        if not username:
            return render(request, 'registration/register.html', {'form': form, 'message': 'username cat not be empty'})
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        except IntegrityError:
            return render(request, "registration/register.html", {
                "message": "Username already taken."
            })
    #     login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'registration/register.html', {'form':form})