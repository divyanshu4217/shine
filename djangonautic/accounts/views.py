from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else :
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{ 'form' : form})
    
# def login_view(request):
#     if request.method == 'POST' :
#         form=UserLoginForm(request.POST)
#         if form.is_valid():
#             user=form.get_user()
#             login(request,user)
#             return redirect('articles:list')
#     else:
#         form = AuthenticationForm()
#     return render(request,'accounts/login.html',{'form':form})