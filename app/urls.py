from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("blogs/", views.blog, name="blog"),
    path("blogs/<slug:slug>/", views.blog_details, name="blog_details"),
    path("contact/", views.contact, name="contact"),
    path("schools/", views.schools, name="schools"),
    path("team/", views.team, name="team"),
    path("change_lang/", views.change_lang, name="change_lang"),
]
# urlpatterns = [
#    url(r'^tinymce/', include('tinymce.urls')),
# ]





