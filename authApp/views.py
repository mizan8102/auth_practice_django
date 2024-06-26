from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            messages.info(request, 'Welcome')
            messages.warning(request, 'This is a warning message')
            form.save()
            print(form.cleaned_data)
    else:
        form = RegisterForm()
        
    return render(request, './signup.html', {'form': form})