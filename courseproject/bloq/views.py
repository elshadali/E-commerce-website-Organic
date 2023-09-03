from django.shortcuts import render
from django.views import generic
from .models import Bloq, Author, Category


def bloqs(request):

    bloq = Bloq.objects.all()
    author = Author.objects.all()
    category = Category.objects.all()

    context = {
        'bloqs' : bloq,
        'authors' : author,
        'categories' : category
    }

    return render(request, 'bloq/bloq.html', context)


class BloqsListView(generic.ListView):
    template_name = 'bloq/bloq.html'
    model = Bloq
    context_object_name = 'bloqs'
    paginate_by = 1
