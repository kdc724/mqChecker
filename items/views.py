from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from . models import Item, Profile
from . forms import ItemForm
from .filters import ItemFilter
from django.http import HttpResponse
import csv


# Create your views here.
@login_required
def index(request):

    items = Item.objects.order_by('-date_checked')


    total_reject = items.filter(status='Reject').count()
    total_monitor = items.filter(status='Monitor').count()
    total_passed = items.filter(status='Passed').count()

    
    latest_items = Item.objects.order_by('-date_checked')[:10]

    context = {
        'items':latest_items,
        'rejects':total_reject,
        'monitor': total_monitor,
        'passed': total_passed,

    }

    return render(request,'items/dashboard.html', context)

@login_required
def detail(request, item_id):

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item
    }

    return render (request,'items/detail.html',context)
@login_required
def check_item (request):
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES,)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.checker = request.user.profile
            instance.save()
            
            return redirect('dashboard')
    else:
        form = ItemForm()
    return render(request, 'items/check.html', {'form': form})

@login_required
def update_item(request, item_id):

	item = Item.objects.get(id=item_id)
	form = ItemForm(instance=item)

	if request.method == 'POST':
		form = ItemForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}
	return render(request, 'items/check.html', context)
@login_required
def delete_item(request, item_id):
	item = Item.objects.get(id=item_id)
	if request.method == "POST":
		item.delete()
		return redirect('dashboard')

	context = {'item':item}
	return render(request, 'items/delete.html', context)

@login_required
def search_item(request):

    items = Item.objects.order_by('-date_checked')
    myFilter = ItemFilter(request.GET, queryset=items)
    items = myFilter.qs
    total_search = items.count()

    paginator = Paginator(items, 15)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)

    context = {
        'items':paged_items,
        'myFilter':myFilter,
        'total_search':total_search

    }

    return render(request,'items/list.html', context)


@login_required
def my_items(request):

    
    user_items = Item.objects.order_by('-date_checked').filter(checker=request.user.profile)
    total_reject = user_items.filter(status='Reject').count()
    total_monitor = user_items.filter(status='Monitor').count()
    total_passed = user_items.filter(status='Passed').count()


    context = {
        'items': user_items,
        'rejects':total_reject,
        'monitor': total_monitor,
        'passed': total_passed,
    }

    return render(request,'items/userdashboard.html',context)

def exporting_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="My Items.csv"'
    writer = csv.writer(response)
    writer.writerow(['TITLE', 'CATEGORY','CONDITION','STATUS','CHECKER','DATE CHECKED','PRIORITY','TEAM','COMMENTS',])

    items = Item.objects.order_by('-date_checked').filter(checker=request.user.profile)

    for item in items:
        writer.writerow([item.title, item.category,item.condition,item.status,item.checker,item.date_checked,item.priority, item.team,item.comments])

    return response

#SEARCH EXPORT TO CSV
#@login_required
#def report(request):

#    items = Item.objects.all()
#    form = ExportForm(request.POST or None)
#    context = {
#        "queryset": items,
#        "form": form,
#    }
#    if request.method == 'POST':
#        queryset = Item.objects.all().order_by('-date_checked').filter(title__icontains=form['title'].value(),category__iexact=form['category'].value())
#
#        context = {
#            "queryset":queryset,
#            "form": form,
#
#        }
#
#        if form['export_csv'].value() == True:
#            response = HttpResponse(content_type='text/csv')
#            response['Content-Disposition'] = 'attachment;filename="Computer list.csv"'
#            writer = csv.writer(response)
#            writer.writerow(['TITLE', 'CATEGORY'])
#            instance = queryset
#            for row in instance:
#                writer.writerow([row.title, row.category])
#
#            return response
#
#    
#
#    return render(request,'items/report.html',context)





