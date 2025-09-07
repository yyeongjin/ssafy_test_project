from django.shortcuts import render, redirect
from .models import demo_model
# Create your views here.
def index(request):
    num_model = demo_model.objects.all()
    context = {
        "num": num_model,
    }
    return render(request, 'index.html', context)

def num(request, num):
    num_model = demo_model.objects.filter(id=num).all()
    context = {
        "num": num_model,
    }
    return render(request, "num.html", context)

def create(request):
    num_model = demo_model()
    num_model.num = request.POST.get('num')
    num_model.destination = request.POST.get('destination')
    num_model.save()
    return redirect('demo_app:index')

def delete(request, num):
    num_model = demo_model.objects.filter(id=num)
    num_model.delete()
    return redirect('demo_app:index')