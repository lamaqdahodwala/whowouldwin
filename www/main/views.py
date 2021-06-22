import django.http
from django.shortcuts import render
from django.views.generic import ListView
from .models import Fight
from .forms import FightForm

# Create your views here.
class Indexview(ListView):
    model = Fight
    template_name = 'main/index.html'
    
def new_fight(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = FightForm(req.POST or None)
            inst = form.save(commit=False)
            inst.op = req.user
            inst.save()
            return django.http.HttpResponseRedirect('/')
        else:
            form = FightForm()
            return render(req, 'main/newfight.html', {'form': form})
    else:
        return django.http.HttpResponseForbidden
    
def view_fight(req, pk):
    fight = Fight.objects.get(pk=pk)
    return render(req, 'main/fight.html', {'fight': fight})