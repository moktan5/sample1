from django.shortcuts import render

# Create your views here.
def login_view(request):
    template_name = 'loginview.html'

    return render(request,template_name)