from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from wiki.forms import PageForm


class HomePage(ListView):

    model = Page

    def get(self, request):
        latest_page_list = Page.objects.order_by('-created')
        context = {'latest_page_list': latest_page_list}
        return render(request, 'wiki/base.html', context)

class PageList(ListView):

    model = Page

    def get(self, request):
        latest_page_list = Page.objects.order_by('-created')
        context = {'latest_page_list': latest_page_list}
        return render(request, 'wiki/list.html', context)
        """ Returns a list of wiki pages. """


class PageDetailView(DetailView):

    model = Page

    def get(self, request, slug):
        page = Page.objects.get(slug=slug)
        form = PageForm(initial={'title': page.title, 'author': page.author, 'slug': page.slug, 'content': page.content})
        return render(request, 'wiki/page.html', {'page': page, 'form': form})

    def post(self, request, slug):
        form = PageForm(request.POST)
        if form.is_valid():
            obj = Page()
            obj.title = form.cleaned_data['title']
            obj.author = form.cleaned_data['author']
            obj.slug = form.cleaned_data['slug']
            obj.email = form.cleaned_data['email']
            obj.content = form.cleaned_data['content']
            obj.save()
            messages.add_message(request, messages.INFO, obj.title+' has been successfully updated')
            return HttpResponseRedirect(reverse('wiki-list-page'))
        else:
            form = PageForm()
            page = Page.objects.get(slug=slug)
            return render(request, 'wiki/page.html', {'page': page, 'form': form})
