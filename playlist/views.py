from django.shortcuts import render
from . import models

def all_ext3mu(request):
    links = models.Link.objects.select_related('channel', 'channel__category').filter(
        is_primary=True, channel__is_active=True
    )
    return render(request, 'playlist/all_ext3mu.html', {'links': links})
