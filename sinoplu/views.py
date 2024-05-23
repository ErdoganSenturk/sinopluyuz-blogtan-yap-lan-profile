from django.shortcuts import render, redirect
from .forms import SinopluForm
from .models import Sinopluyuz
from .filters import SinopluFilter


def index(request):
    return render(request, 'sinoplu/index.html')


def sinoplu_list(request):
    sinoplular=Sinopluyuz.objects.all()
    context={
        'sinoplular':sinoplular
    }
    return render(request,'sinoplu/sinoplu_list.html', context)


def sinoplu_add(request):
    form=SinopluForm()
    if request.method=='POST':
        form=SinopluForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context={
      'form':form  
    }
    return render(request,'sinoplu/sinoplu_add.html',context)


def sinoplu_update(request, id):
    sinoplu=Sinopluyuz.objects.get(id=id)
    form=SinopluForm(instance=sinoplu)
    if request.method=='POST':
        form=SinopluForm(request.POST,instance=sinoplu)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context={
        'form':form
    }
    return render(request,'sinoplu/sinoplu_update.html',context)


def sinoplu_delete(request,id):
    sinoplu=Sinopluyuz.objects.get(id=id)
    if request.method=='POST':
        sinoplu.delete()
        return redirect("list")  
        
    context={
            'sinoplu':sinoplu
    }
    return render(request,"sinoplu/sinoplu_delete.html",context)


def sinoplu_detail(request, id):        
    sinoplu = Sinopluyuz.objects.get(id=id)
    context = {
        'sinoplu': sinoplu
    }
    return render(request, 'sinoplu/sinoplu_detail.html', context)


def filter_list(request):
    # sinoplu_filter = Sinopluyuz.objects.all()
    filtered_sinoplu = SinopluFilter(request.GET)
    return render(request, 'sinoplu/sinoplu_filter.html', {'filter': filtered_sinoplu})

