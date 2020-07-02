from django.shortcuts import render
from django.http import JsonResponse
from .models import  *

def index(request):
    post=Post.objects.all();
    events=Events.objects.all();
    context=dict(posts=post,event=events)
    return render(request,"views/index.html",context)
def contact_us(request):
    return render(request,"views/contact.html")
def about_us(request):
    return render(request,"views/about.html")
def login(request):
    return render(request,"views/index.html")
def message(request):
    print(request.POST)
    contexts=dict(response="Thanks for your message")
    return JsonResponse(contexts)
def sermon(request):
    return render(request,"views/sermons.html")
def events(request):
    return render(request,"views/events.html")
def post_detail(request,id):
    post=Post.objects.get(id=id);
    context=dict(posts=post)
    return render(request, "views/posts.html",context)
