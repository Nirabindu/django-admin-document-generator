from django.shortcuts import render

# Create your views here.


def homepage(request):
    
    '''
    Function responds to website root HTTP requests
    
    Return index html pages -no db required
    '''
    return render(request)