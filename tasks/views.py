from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from tasks.models import Tasks

# Create your views here.
def home(request):
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        tasks=Tasks(title=title,desc=desc)
        tasks.save()
        dic={'tasks':True}
    else:
        dic={}
    return render(request,'home.html',dic)

def tasks(request):
    taskdata=Tasks.objects.all()
    context={'task':taskdata}
    return render(request,'tasks.html',context)


def delete(request,pk):
    obj=Tasks.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('home')
    
    object={'obj':obj}
    return render(request,'delete.html',object)