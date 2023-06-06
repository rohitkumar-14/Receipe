from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def receipes(request):
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        recepie = Receipe.objects.create(
            receipe_name=receipe_name, receipe_description=receipe_description, receipe_image=receipe_image)

        return redirect('/')
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            receipe_name__icontains=request.GET.get('search'))

    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)


def delete(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')
