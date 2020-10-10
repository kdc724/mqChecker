from django.shortcuts import render
from . models import Announcement
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def index(request):
  announcements = Announcement.objects.order_by('-date_created').filter(is_published=True)

  paginator = Paginator(announcements, 15)
  page = request.GET.get('page')
  paged_announcements = paginator.get_page(page)

  context = {
    'announcements': paged_announcements,
  }

  return render(request,'announcements/announcement.html', context)
