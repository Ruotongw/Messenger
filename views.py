from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from .models import Message
from django import forms


@login_required
def home(request):
    return render(request, 'messenger/home.html')

# sign up page 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'messenger/signup.html', {'form': form})

# create a new message, with users names option 
def newMessage(request):
    users=User.objects.all()
    if request.method == 'POST':
        form = request.POST
        sender = form.get('sender')
        message = form.get('message')
        receiver = form.get('receiver')
        # print(request.user)
        sent = form.get("sent")
        u=User.objects.get(username=sender)   
        s=User.objects.get(username=receiver)
        q = Message(text=message, sent=sent, date=timezone.now(), sender=u, receiver=s)
        q.save()
        # print(q.get('message'))
        return render(request, 'messenger/home.html')
    return render(request,'messenger/message.html',{'users':users,'message':''})

# edit the message 
def editMessage(request, message_id):
    users=User.objects.all()
    print(message_id)
    Messages = Message.objects.get(id=message_id)
    print(Messages.text)
    return render(request,'messenger/message.html',{'users':users,'message':Messages})

# view all the messages 
def viewMessage(request):
    sent = Message.objects.filter(sender=request.user).filter(sent=True)
    drafts = Message.objects.filter(sender=request.user).filter(sent=False)
    receive = Message.objects.filter(receiver=request.user).filter(sent=True)
    return render(request,'messenger/viewMessages.html',{'sent': sent,'drafts':drafts,'receive':receive})
