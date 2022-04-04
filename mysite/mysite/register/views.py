from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm( request.POST )
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get( 'username' )
            messages.success( request, f'Welcome {user_name}. Your are currentlly loged in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render( request, 'user/register.html', {'form' : form} )