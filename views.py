from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html', {})


def about_company(request):
    return render(request, 'about_company.html', {})