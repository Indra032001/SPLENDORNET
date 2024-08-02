from django.shortcuts import render, redirect
from .models import MRSystem
from .forms import MRSForm


def Show_View(request):
    template_name = 'MRSApp/Show.html'
    obj = MRSystem.objects.all()
    context = {'obj': obj}
    return render(request, template_name, context)


def Add_View(request):
    if request.method == "GET":
        template_name = 'MRSApp/Add.html'
        form = MRSForm()
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == "POST":
        filled_form = MRSForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('/revivew/show/')


def Update_view(request, i):
    if request.method == "GET":
        template_name = 'MRSApp/Add.html'
        Order_obj = MRSystem.objects.get(id=i)
        form = MRSForm(instance=Order_obj)
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == "POST":
        Order_obj = MRSystem.objects.get(id=i)
        filled_form = MRSForm(request.POST, instance=Order_obj)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('/revivew/show/')


def Delete_view(request, i):
    Order_obj = MRSystem.objects.get(id=i)
    Order_obj.delete()
    return redirect('/revivew/show/')