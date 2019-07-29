from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Title, Body

class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'titles'

    def get_queryset(self): 
        return Title.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Title
    template_name = 'blogs/detail.html'

def create(request):
    return render(request, 'blogs/create.html')




def save(request):
    title_text = request.POST['title_text']
    body_text = request.POST['body_text']

    title = Title(title_text=title_text)
    title.save()

    title = Title.objects.latest('id')

    body = Body(body_text=body_text, title=title)
    body.save()

    return HttpResponseRedirect(reverse('blogs:index'))

