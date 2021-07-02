import django.http
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Fight
from .forms import FightForm

# Create your views here.
class Indexview(ListView):
    model = Fight
    template_name = "main/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        context["object_list"] = Fight.objects.order_by("-id")
        return context


def new_fight(req):
        if req.method == "POST":
            form = FightForm(req.POST or None)
            inst = form.save(commit=False)
            inst.op = req.user
            inst.save()
            return django.http.HttpResponseRedirect("/")
        else:
            form = FightForm()
            return render(req, "main/newfight.html", {"form": form})

def red_vote(req, pk):
    if req.method == 'POST' and req.user.is_authenticated:
        fight = get_object_or_404(Fight, id=req.POST.get('fight_id'))
        voted = False
        if fight.red_votes.filter(id=req.user.id).exists():
            fight.red_votes.remove(req.user)
            voted = False
        else:
            if fight.blue_votes.filter(id=req.user.id).exists():
                fight.blue_votes.remove(req.user)
            fight.red_votes.add(req.user)
        fight.save()
        return HttpResponseRedirect(f'/fight/{pk}')
    else:
        return HttpResponseForbidden()

def blue_vote(req, pk):
    if req.method == 'POST' and req.user.is_authenticated:
        fight = get_object_or_404(Fight, id=req.POST.get('fight_id'))
        voted = False
        if fight.blue_votes.filter(id=req.user.id).exists():
            fight.blue_votes.remove(req.user)
            voted = False
        else:
            voted = True
            if fight.red_votes.filter(id=req.user.id).exists():
                fight.red_votes.remove(req.user)

            fight.blue_votes.add(req.user)
        fight.save()
        return HttpResponseRedirect(f'/fight/{pk}')
    else:
        return HttpResponseForbidden()

def view_fight(req, pk):
    fight:Fight = Fight.objects.get(pk=pk)
    voted_blue, voted_red = False, False
    if fight.blue_votes.filter(id=req.user.id).exists():
        voted_blue = True
        voted_red = False
    
    if fight.red_votes.filter(id=req.user.id).exists():
        voted_red=True
        voted_blue=False
    
    return render(req, "main/fight.html", {"fight": fight, "voted_blue": voted_blue, "voted_red": voted_red})
