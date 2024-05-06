from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def profile(request):
    context = {} 
    return render(request, 'base/calculator.html', context)


def calculate(request):
    if request.method=='POST':
        number_one=request.POST.get("number_one")
        number_two=request.POST.get("number_two")
        operation=request.POST.get("operation")
    
    if operation=="add":
        result = float(number_one)+float(number_two)
        context={'result':result}
        return render( request ,"base/calculator.html",context)
    
    elif operation=="subtract":
        result = float(number_one)-float(number_two)
        context={'result':result}
        return render( request ,"base/calculator.html",context)
    
    elif operation=="multiply":
        result = float(number_one)*float(number_two)
        context={'result':result}
        return render( request ,"base/calculator.html",context)
    
    elif operation=="divide":
        result = float(number_one)/float(number_two)
        context={'result':result}
        return render( request ,"base/calculator.html",context)

    else:
        return HttpResponse('calculator.html') 
    
