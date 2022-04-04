from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Class based ListView
class TaskListview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

# Class Based DetailView
class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'i'

# Class update views
class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk':self.object.id})

# Delete views
class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')




# task adding.
def note(request):
    display = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task', '')
        priority=request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task=Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'task': display})

#def details(request):
#    task=Task.objects.all()
#    return render(request, 'details.html', {'task': task})

#deleting file
def delete(request, taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return  render(request, 'delete.html')

#Update funtion
def update(request, id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})
