from django.shortcuts import render

def index(request):
    # Just render the index template.
    return render(request, 'index.html', context)

