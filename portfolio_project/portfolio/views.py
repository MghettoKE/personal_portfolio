from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
#save the contact message to the database
            return render(request,'portfolio/contact.html',{'form':ContactForm(),'message':'success'})
        else:
            return render(request,'portfolio/contact.html',{'form':form,'message':'error'})
    else:
        form = ContactForm()
        return render(request,'portfolio/contact.html',{'form':form})





