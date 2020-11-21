from django.shortcuts import render, redirect

# Create your views here.

from django.views import generic
from django import forms

from django.utils import timezone
import sqlite3

class adpost_view(generic.View):

    template_name = "adddrop.html"

    def get(self, request):
        
        return render(request, self.template_name)

    def post(self,request):
        if request.method == 'POST':
            
            conn = sqlite3.connect('db.sqlite3')
            c = conn.cursor()

            title = request.POST.get('Title','')
            location = request.POST.get('Location','')
            caption = request.POST.get('Caption','')
            created_on = timezone.now()
            curr_user = request.user
            author_id = curr_user.id

            c.execute("INSERT INTO oceanapp_oceanappmodel (title, location, caption, created_on, author_id) VALUES (?, ?, ?, ?, ?)", (title, location, caption, created_on, author_id))

            conn.commit()
            
            conn.close()
            return redirect('/Home/')
        else:
            return render(request, self.template_name)


            

