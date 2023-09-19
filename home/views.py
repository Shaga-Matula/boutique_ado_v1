from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Veiw to return render page
    """
    return render(request, 'home/index.html')
