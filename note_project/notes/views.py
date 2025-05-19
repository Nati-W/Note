from django.shortcuts import render
from .models import note

# Create your views here.
def home(request):
    notes = note.objects.all()
    return render(request, 'notes/notes.html', { 'notes':notes })