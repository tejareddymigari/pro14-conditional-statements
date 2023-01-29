from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':230,'b':40,'c':90}
    return render(request,'operations.html',d)