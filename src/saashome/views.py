import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits


this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request,*args, **kwargs):
    return about_view(request, *args, **kwargs)
    
    

def about_view(request):
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path = request.path)
    my_title = "My Page"
    PageVisits.objects.create(path=request.path )
    content = {
        "page_title" : my_title,
        "page_visit_count" : page_qs.count(),
        "total_visit_count" : qs.count(),
    }    
    return render(request , "home.html" , content)