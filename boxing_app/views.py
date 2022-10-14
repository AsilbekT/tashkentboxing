from django.shortcuts import redirect, render

from boxing_app.forms import BoxerForm
from .models import *
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.utils import translation
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/base/login/')
def index(request):
    return render(request, "base/admin_lte/index.html")

@login_required(login_url='/base/login/')
def main_page(request):
    regions = Viloyatlar.objects.all()
    boxers = Boxer.objects.all()
    all_types_of_chempion = All_types_of_chempion.objects.all()
    if request.method == "POST":
        regions_list = request.POST.getlist('regions')
        chempion_type = request.POST.getlist('chempion_type')
        regions_list_obj = Viloyatlar.objects.filter(viloyat_nomi_uz__in=regions_list)
        regions_list_obj_ids = [x.id for x in regions_list_obj]
        
        if len(chempion_type) > 0:
            chempion_people = All_types_of_chempion.objects.get(type_uz=chempion_type[0])
            boxers = Boxer.objects.filter(viloyat__in=regions_list_obj_ids, unvoni=chempion_people.id)
        else:
            boxers = Boxer.objects.filter(viloyat__in=regions_list_obj_ids)

    context = {"boxers": boxers, "regions": regions, 'chempion_type': all_types_of_chempion}
    return render(request, "base/admin_lte/data.html", context)

@login_required(login_url='/base/login/')
def boxers_details(request, id):
    boxer = Boxer.objects.get(id=id)


    context = {"boxer": boxer}
    return render(request, "base/details/index.html", context)

@login_required(login_url='/base/login/')
def edit_boxer(request, id):
    boxer = Boxer.objects.get(id=id)

    context = {"boxer": boxer}
    return render(request, "base/details/form_edit.html", context)

@login_required(login_url='/base/login/')
def add_boxer(request):
    
    if request.method == "POST":
        form = BoxerForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
    form = BoxerForm()

    context = {"form": form}
    return render(request, "base/details/form.html", context)


def auth_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect("main_page")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "base/admin_lte/pages/examples/login.html", context={"login_form":form})


def change_lang(request):
    LANGUAGE_SESSION_KEY = '_language'
    if request.method == "POST":
        sent_url = request.POST['next']
        old_lang = request.LANGUAGE_CODE
        changed_lang = request.POST['language']
        translation.activate(changed_lang)
        request.session[LANGUAGE_SESSION_KEY] = changed_lang
        # # I use HTTP_REFERER to direct them back to previous path 
        if "en" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url.replace('en', changed_lang)
                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url.replace('en', '')
                new_url = new_url1[1:]
                return HttpResponseRedirect(new_url)
        elif "ru" in sent_url:
            if changed_lang != 'uz':
                new_url = sent_url.replace('ru', changed_lang)
                return HttpResponseRedirect(new_url)
            elif changed_lang == 'uz':
                new_url1 = sent_url.replace('ru', '')
                new_url = new_url1[1:]
                return HttpResponseRedirect(new_url)
        elif old_lang == "uz" and changed_lang != 'uz':
            new_url = f"/{changed_lang}" + sent_url

            return HttpResponseRedirect(new_url)
        
        return HttpResponseRedirect(sent_url)





# translation main page
# left nav bar links
# edit details