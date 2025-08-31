from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    queryvisit = PageVisit.objects.all()
    my_title = "mere homme pagr"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryvisit.count()
    }
    home_template = "home.html"
    PageVisit.objects.create()
    return render(request, home_template, my_context)