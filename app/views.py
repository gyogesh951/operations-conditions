from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':18,'b':20,'c':30}
    return render(request,'operations.html',d)