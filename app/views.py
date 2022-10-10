from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import ContactForm
from .models import Blog, Members, School
import requests
from .credentials import TOKEN
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.utils import translation
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
# Create your views here.


def index(request):
    blogs = Blog.objects.all().order_by('-id')[:5]
    members = Members.objects.all()
    schools = School.objects.all()
    context = {"schools": schools, "blogs": blogs, 'members': members}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, "blog.html", context)

    
def blog_details(request, slug):
    print(slug)
    blog = Blog.objects.get(slug=slug)
    context = {"blog": blog}
    return render(request, "blog_details.html", context)




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
          
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            surname = data['surname']
            number = data['number']
            email = data['email']
            message = data['message']
            text = f"<b>Ism:</b> {name}\n<b>Familya:</b> {surname}\n<b>Nomeri:</b> {number}\n<b>Email:</b> {email}\n<b>Texti:</b> {message}\n"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=-807707176&parse_mode=html&text={text}"
            requests.post(url)
            return redirect("home")
        else:
            return HttpResponse("OOPS! Bot suspected.")
            
    else:
        form = ContactForm()
          
    return render(request, 'contact.html', {'form':form})


def schools(request):
    schools = School.objects.all()
    context = {"schools": schools}
    return render(request, "schools.html", context)


def team(request):
    members = Members.objects.all()

    context = {"members": members}
    return render(request, "team.html", context)



def change_lang(request):
    LANGUAGE_SESSION_KEY = '_language'
    if request.method == "POST":
        sent_url = request.POST['next']
        old_lang = request.LANGUAGE_CODE
        changed_lang = request.POST['language']
        translation.activate(changed_lang)
        request.session[LANGUAGE_SESSION_KEY] = changed_lang
        url_details = sent_url.split('/')[1:-1]
        
        # # I use HTTP_REFERER to direct them back to previous path 
        if "en/" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url[0:4].replace('en', changed_lang)
                if len(url_details) > 2:
                    new_url += url_details[1] + "/" + url_details[2] + "/"
                elif len(url_details) > 1:
                    new_url += url_details[1] + "/"

                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url[0:4].replace('en', '')
                new_url = new_url1[1:]
                if len(url_details) > 2:
                    new_url += url_details[1] + "/" + url_details[2] + "/"
                elif len(url_details) > 1:
                    new_url += url_details[1] + "/"
                return HttpResponseRedirect(new_url)
        elif "ru/" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url[0:4].replace('ru', changed_lang)
                if len(url_details) > 2:
                    new_url += url_details[1] + "/" + url_details[2] + "/"
                elif len(url_details) > 1:
                    new_url += url_details[1] + "/"
                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url[0:4].replace('ru', '')
                new_url = new_url1[1:]
                if len(url_details) > 2:
                    new_url += url_details[1] + "/" + url_details[2] + "/"
                elif len(url_details) > 1:
                    new_url += url_details[1] + "/"
                return HttpResponseRedirect(new_url)
        elif old_lang == "uz" and changed_lang != 'uz':
            new_url = f"/{changed_lang}" + sent_url

            return HttpResponseRedirect(new_url)
        
        return HttpResponseRedirect(sent_url)

