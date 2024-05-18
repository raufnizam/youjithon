from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):

    today = date.today()
    hackathons = Hackathon.objects.all()
    context ={
        'hackathons': hackathons,
        'today': today
        }

    return render(request,'index.html', context)

def rules(request):
    return render(request,'rules.html')

def faq(request):
    return render(request,'faq.html')

def grading(request):
    return render(request,'grading.html')

def hackathon_history(request):
    return render(request,'hackathon/hackathon_history.html')


from .models import Hackathon

def hackathon(request):
    hackathons = Hackathon.objects.all()
    return render(request, 'hackathon/hackathon.html', {'hackathons': hackathons})


# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Hackathon
from .forms import HackathonForm

def hackathon_add(request):
    if request.method == 'POST':
        form = HackathonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hackathon')
    else:
        form = HackathonForm()
    return render(request, 'hackathon/hackathon_add.html', {'form': form})

def hackathon_edit(request, hackathon_id):
    hackathon = get_object_or_404(Hackathon, id=hackathon_id)
    if request.method == 'POST':
        form = HackathonForm(request.POST, instance=hackathon)
        if form.is_valid():
            form.save()
            return redirect('hackathon')
    else:
        form = HackathonForm(instance=hackathon)
    return render(request, 'hackathon/hackathon_edit.html', {'form': form})

def hackathon_remove(request, hackathon_id):
    hackathon = get_object_or_404(Hackathon, id=hackathon_id)
    if request.method == 'POST':
        hackathon.delete()
        return redirect('hackathon')
    return render(request, 'hackathon/hackathon_remove.html', {'hackathon': hackathon})
