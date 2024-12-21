from django.shortcuts import render, get_object_or_404
from .models import Page

def page_detail(request, path):
    slug_path = path.strip('/').split('/')
    page = None
    for slug in slug_path:
        if page is None:
            page = get_object_or_404(Page, slug=slug, parent=None)
        else:
            page = get_object_or_404(Page, slug=slug, parent=page)
    return render(request, 'page_detail.html', {'page': page})