from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello_world.html', {})

def about_company(request):
    return render(request, 'about_company.html', {})

def our_team(request):
    return render(request, 'our_team.html', {})

def contact_us(request):
    return render(request, 'contact_us.html', {})

def news(request):
    return render(request, 'news.html', {})