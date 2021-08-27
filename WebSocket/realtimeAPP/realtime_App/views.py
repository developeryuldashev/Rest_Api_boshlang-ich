from django.shortcuts import render
def index(request):
    return render(request, 'index.html',{'text':"Assalomu alekum Men Dilshod Yo'ldoshev."})
