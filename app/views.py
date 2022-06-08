from app.forms import CommentForm, MailingListForm, ReplyForm
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail


# auth      


def index(request):
    mForm = MailingListForm()
    return render(request, 'index.html',{"mForm":mForm})

def about(request):
    mForm = MailingListForm()
    return render(request, 'about.html', {"mForm":mForm})

def solutions(request):
    mForm = MailingListForm()
    return render (request, 'solution.html',{"mForm":mForm})

def contact(request):
    mForm = MailingListForm()
    return render (request, 'contact.html',{"mForm":mForm})

def blogs(request):
    mForm = MailingListForm()
    posts = Blogs.objects.all()
    form = ReplyForm()
    if request.method == 'POST':  
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('blogs')
    print(posts)
    ctx= {
        "posts":posts,
        "form":form,
        "mForm":mForm,
    }
    return render (request, 'blog.html', ctx )

def blogDetails(request,blogs_id):
    mForm = MailingListForm()
    posts = Blogs.objects.all()
    form = ReplyForm()
    blog = Blogs.objects.filter(pk = blogs_id)
    if request.method == 'POST':  
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('blogs')
    print(posts)
    ctx= {
        "posts":posts,
        "form":form,
        "blog":blog,
        "mForm":mForm,
    }
    return render (request, 'blog-details.html', ctx)

def blogDetails(request, blogs_id):
    mForm = MailingListForm()
    posts = Blogs.objects.all()
    form = ReplyForm()
    blog = Blogs.objects.filter(pk = blogs_id)
    if request.method == 'POST':  
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('blogs')
    print(posts)
    ctx= {
        "posts":posts,
        "form":form,
        "blog":blog,
        "mForm":mForm,
    }
    return render (request, 'blog-details.html', ctx)

def comments(request, blogs_id):
  form = ReplyForm()
  post = Blogs.objects.filter(pk = blogs_id).first()
  if request.method == 'POST':
    form = ReplyForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.blog = post
      comment.save() 
  return redirect('blogDetails', blogs_id=blogs_id) 
 


def addMailingList(request, reverse):
    mForm = MailingListForm()
    if request.method == "POST":
        mForm = MailingListForm(request.POST)
        if mForm.is_valid():
            mForm.save(commit=True)
            return redirect(reverse)


def sendMails(request):
    mails = MailingList.objects.all()
    send_mail("subject", "message", "erdeminsurance22@gmail.com", mails)
    return redirect("/")