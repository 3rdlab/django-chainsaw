from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Board

class IndexView(generic.ListView):
    template_name = 'board/index.html'
    context_object_name = 'latest_list'

    def get_queryset(self):
        return Board.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Board
    template_name = 'board/detail.html'


def register(request):
    if request.method == "POST":
        """ form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=false)
            post.author = request.user
            post.pub_date = datetime.datetime.now()
            post.save() """
        return HttpResponseRedirect(reverse('board:detail', args=post.pk))
    else:
        # form = PostForm()
        return render(request, 'board/register.html', {'form': 'form'})
