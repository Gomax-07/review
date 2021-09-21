from django.shortcuts import render, redirect
from projects.models import Project, Image, Location
from django.http import HttpResponse
from .forms import ImageForm
from django.views.generic import ListView, CreateView  # new
from django.urls import reverse_lazy  # new


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


class ImageModel:
    pass


def home_view(request):
    context = {}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


class HomePageView(ListView):
    model = Image
    template_name = 'home.html'


def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def image_detail(request, pk):
    image = Image.objects.get(pk=pk)
    location = Location.objects.get(pk=pk)
    context = {
        'image': image,
        'location': location
    }
    return render(request, 'image_details.html', context)


def image_index(request):
    images = Image.objects.all()
    context = {
        'images': images
    }
    return render(request, 'home.html', context)