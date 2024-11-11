from django.shortcuts import render

def main_page(request):
    return render(request, 'main_page.html')

def user_join(request):
    return render(request, 'user_join.html')