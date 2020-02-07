from django.shortcuts import render
from django.http import HttpResponse
from .formal import ContactForm
def tweek_view(request):
    return render(request,"test.html",{"var1" : 1 ,"var2": ' ','val ':3, 'lis' : enumerate([1,2,3,4])})

def homepage_view(request):
    return HttpResponse("Hi, to homepage")

def about_view(request):
    return render(request,'about.html')

def anti_view(request):
    return render(request,'anti.html')


def form_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            return redirect('tesaroo : tweek ')
    else :
        form = ContactForm()
    return render(request,'forms.html',{'form' : form})
    