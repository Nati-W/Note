from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib. auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.save())
            return redirect(reversed('notes_app:homes'))
        else:
            form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'users/register.html', { 'form':form })