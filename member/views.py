from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    # username = request.POST.get('username')
    # password1 = request.POST.get('password1')
    # password2 = request.POST.get('password2')
    # print(username)
    # print(password1)
    # print(password2)

    # username 중복 확인 작업
    # pw 1,2 일치 확인 작업
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/users/login/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)