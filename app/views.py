from django.shortcuts import render

# Create your views here.
def Built_in_filters(request):
    d={'data':'hai PYTHON how R You','c':10}
    return render(request,'Built_in_filters.html',d)

def userdefinedfilters(request):
    d={'data':'HI Python HoW R yoU'}
    return render(request,'userdefinedfilters.html',d)