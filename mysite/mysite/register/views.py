from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get( 'username' )
            messages.success( request, f'Welcome {user_name}. Your account is successfully created')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render( request, 'user/register.html', {'form' : form} )