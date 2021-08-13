from django.shortcuts import render

# Create your views here.
def app1_ht1(request):
    return render(request, 'first.html')