import django.http
from django.http import HttpResponseRedirect
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
    if req.user.is_authenticated:
        if req.method == "POST":
            form = FightForm(req.POST or None)
            inst = form.save(commit=False)
            inst.op = req.user
            inst.save()
            return django.http.HttpResponseRedirect("/")
        else:
            form = FightForm()
            return render(req, "main/newfight.html", {"form": form})
    else:
        return django.http.HttpResponseForbidden

def red_vote(req, pk):
    fight = get_object_or_404(Fight, id=req.POST.get('fight_id'))
    voted = False
    if fight.red_votes.filter(id=req.user.id).exists():
        fight.red_votes.remove(req.user)
        voted = False
    else:
        voted = True
        fight.red_votes.add(req.user)
    fight.save()
    return HttpResponseRedirect(f'/fight/{pk}')

def blue_vote(req, pk):
    fight = get_object_or_404(Fight, id=req.POST.get('fight_id'))
    voted = False
    if fight.blue_votes.filter(id=req.user.id).exists():
        fight.blue_votes.remove(req.user)
        voted = False
    else:
        voted = True
        fight.blue_votes.add(req.user)
    fight.save()
    return HttpResponseRedirect(f'/fight/{pk}')

def view_fight(req, pk):
    fight = Fight.objects.get(pk=pk)
    return render(req, "main/fight.html", {"fight": fight})
