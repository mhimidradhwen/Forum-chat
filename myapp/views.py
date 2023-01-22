from django.shortcuts import render, redirect
from .models import Message, Sender

def home(request):
    messages = Message.objects.all()    
    context = {'messages': messages}
    if request.method == "POST":
        content = request.POST.get("content", False)
        sender_name = request.POST.get("sender_name", False)
        
        if sender_name =="":
                sender_name = "guest"
        sender = Sender.objects.get(name=sender_name)
        
        
        if content != "":
            new_message = Message(content=content, sender=sender)
            new_message.save()
            return redirect("home")
    return render(request, "myapp/home.html", context)

def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    message.delete()
    return redirect("home")

def join_username(request):
    if request.method == "POST":
        name = request.POST.get("username",False)
        color = request.POST.get("color",False)
        new_user = Sender(name=name, message_color=color)
        new_user.save()
        context={"user":new_user.name}
        return redirect("home")
        # return render(request,"myapp/home.html",context={"user":new_user})
    return render(request, "myapp/login.html")
