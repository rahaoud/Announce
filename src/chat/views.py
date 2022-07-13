from django.shortcuts import render
from .models import Thread, Message
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/admin')
def index(request):
    threads = Thread.objects.all()
    context = {"threads": threads}
    return render(request, 'chat/index.html', context)


@login_required(login_url='/admin')
def detail(request, id):
    thread = Thread.objects.get(id=id)
    if request.method == "POST":
        message = request.POST.get("message")
        sender = request.user
        Message.objects.create(thread=thread, sender=sender, message=message)
    context = {"thread": thread}
    messages = Message.objects.filter(thread=thread)
    context["messages"] = messages
    template = 'chat/thread.html'
    return render(request, template, context)
