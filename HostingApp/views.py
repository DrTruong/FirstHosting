from django.shortcuts import render

# Create your views here.
def hostingApp(request):
    return render(request, 'hostingApp.html', {})