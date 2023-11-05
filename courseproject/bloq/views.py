from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Bloq, Author, Category


def bloq_detail(request, bloq_slug):

    bloq = Bloq.objects.get(slug=bloq_slug)
    author = Author.objects.all()
    category = Category.objects.all()
    blog_categories_ids = [cat.id for cat in bloq.category.all()]
    relate_blogs = Bloq.objects.filter(category__in=blog_categories_ids).exclude(id=bloq.id).distinct()

    context = {
        'bloq' : bloq,
        'authors' : author,
        'categories' : category,
        'relate_blogs': relate_blogs
    }

    return render(request, 'bloq/bloq_detail.html', context)

class BloqsListView(generic.ListView):
    template_name = 'bloq/bloq.html'
    model = Bloq
    context_object_name = 'bloqs'
    paginate_by = 2
