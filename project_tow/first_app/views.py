from django.shortcuts import render
from django.http import HttpResponse

def indx(request):
    #return HttpResponse('my second project')
    data = {
        'username' : 'ahmad',
        'email' : "ahmad@gmail.com",
        'courses' : ['java', 'python', 'c#']

    }
    
    return render(request, 'indx.html', context=data)

def abuot(request):
    return render(request, 'abuot html')

def contact(request):
    return render(request, 'contact.html')


    


# Create your views here.
