from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.models import Task

from . forms import Todoform
from django.views.generic import ListView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView

# Create your views here.
class taskListView(ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task1'

class taskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task1'

class taskUpdateView(UpdateView):
    model = Task
    template_name = 'update1.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detail1',kwargs={'pk':self.object.id})

class taskDeleteView(DeleteView):
    model = Task
    template_name = 'delete1.html'
    success_url = reverse_lazy('home1')

def index(request):
    task1 = Task.objects.all()
    if request.method=="POST":
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()

    return render(request, 'task.html',{'task1':task1})

def delete(request,delid):
    task = Task.objects.get(id=delid)
    if request.method =="POST":
        task.delete()
        return redirect("/")
    return render(request,'delete.html')

def update(request,id):
    task = Task.objects.get(id=id)
    f = Todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task})
