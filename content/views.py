from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from LoggingActivity.models import LogUserActivity
from content.models import Content


class ContentListView(ListView):
    model = Content
    template_name = 'content/home.html'


class ContentDetailView(DetailView):
    model = Content
    template_name = 'content/content.html'


def management_page(request):
    contents = Content.objects.all()
    logs = LogUserActivity.objects.all()
    return render(request, 'content/management-page.html', {'contents': contents, 'logs': logs})


def delete_content(request, pk):
    content = Content.objects.get(id=pk)
    content.delete()
    return redirect('content:management')
