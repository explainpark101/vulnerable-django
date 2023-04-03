from django.shortcuts import render

def sqlInjection(request):
    context = {}
    
    return render(request, "sqlinjection.html", context)
    