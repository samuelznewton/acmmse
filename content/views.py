from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import About_Pages, File, Announcement, Officer, Conference, ImageContent
from django.conf import settings
# Create your views here.

def announcements(request):
    a = Announcement.objects.all()
    return render(
    request=request,
    template_name="content/announcements.html",
    context={"announcements":a,"images":ImageContent.objects.all()}
    )

def aboutacm(request):
    a = About_Pages.objects.get(page='ACM')
    return render(
    request=request,
    template_name="content/about.html",
    context={"p":a,"images":ImageContent.objects.all()}
    )

def aboutmse(request):
    a = About_Pages.objects.get(page='MSE')
    return render(
    request=request,
    template_name="content/about.html",
    context={"p":a,"images":ImageContent.objects.all()}
    )

def officers(request):
    a = Officer.objects.all()
    return render(
    request=request,
    template_name="content/officers.html",
    context={"officers":a}
    )

def conference(request):
    a = Conference.objects.all().order_by('-year')[0]
    return render(
    request=request,
    template_name="content/conference.html",
    context={"c":a,"images":ImageContent.objects.all()}
    )

def pastyear(request, slug):
    a = Conference.objects.get(year=slug)
    return render(
    request=request,
    template_name="content/conference.html",
    context={"c":a,"images":ImageContent.objects.all()}
    )

def pastcon(request):
    a = Conference.objects.all()
    return render(
    request=request,
    template_name="content/pastcon.html",
    context={"conferences":a}
    )

def documents(request):
    a = File.objects.all()
    return render(
    request=request,
    template_name="content/documents.html",
    context={"documents":a}
    )
