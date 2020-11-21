from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.
from django.views import generic
from .models import oceanappmodel
from django import forms

from django.utils import timezone
import sqlite3


def MyPosts(request):
    if request.method == "POST":
            conn = sqlite3.connect('db.sqlite3')
            c = conn.cursor()
            title = request.POST.get('deletedrop','')
            c.execute("DELETE FROM oceanapp_oceanappmodel WHERE title=?", (title,))
            conn.commit()
            conn.close()
            return redirect('/Home/')
            
    else:
            curr_user = request.user
            author_id = curr_user.id
            querypost = oceanappmodel.objects.filter(author_id = author_id).order_by('-created_on')
            context = {'querypost': querypost}
            return render(request, "mypost.html", context)
            
def PostList(request):
    queryset = oceanappmodel.objects.all().order_by('-created_on')
    context = {'queryset': queryset}
    return render(request, "index.html", context)

def AboutOcean(request):

        return render(request, "aboutus.html")
