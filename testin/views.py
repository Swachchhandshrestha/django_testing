from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title="hello there"
    context = {"title": "Example"}
    template_name = "title.txt"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)

def about_page(request):
    return render(request, "about.html", {"title": "About Us"})

def contact_page(request):
    return render(request, "hello_world.html", {"title": "contact us"})

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
