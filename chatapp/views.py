from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ChatRoom,ChatMessage

# Create your views here.
from .forms import CreateForm
from django.contrib.auth.decorators import login_required


@login_required 
def createroom(request):
   
    form = CreateForm(request.POST or None)
    context = {
        'form':form,
    }
    if form.is_valid():
        form.save()
        return redirect('chatapp:index')
    return render(request,'chatapp/chatform.html',{'form':form})
    
@login_required
def index(request):
    
    chatrooms = ChatRoom.objects.all()
    return render(request,'chatapp/index.html',{'chatrooms':chatrooms})
    
@login_required
def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request,'chatapp/room.html',{'chatroom':chatroom,'messages':messages})