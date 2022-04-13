from django.shortcuts import render, get_object_or_404, redirect
from .models import Participant
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from .forms import RegisForm 
from django.db.models import Q

# Create your views here.

def home_page(request, *args, **kwargs):
    all_items = Participant.objects.filter(Available=True).order_by('-Created_on')[:30]
    paginator = Paginator(all_items, 25) #for paginator to display 25 items on each page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_items' : all_items,
        'page_obj' : page_obj
    }
    return render(request, 'main/home.html', context=context)

def customer_page(request, identity=None):
    customers = get_object_or_404(Participant, identity=identity)
    context = {
        'customers' : customers,
    }
    return render(request, 'main/customer.html', context=context)


def dashboard_page(request, *args, **kwargs):
    return render(request, 'main/dashboard.html', {})

def lead_party(request, *args, **kwargs):
    return render(request, 'main/leadparty.html', {})


class SearchResultView(ListView):
    model = Participant
    template_name = 'main/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Participant.objects.filter(
            Q(Status__icontains=query)
        )
        return object_list

def register_page(request, *args, **kwargs):

    form = RegisForm()

    if request.method == "POST":
        form = RegisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        user = form.cleaned_data.get('username')
        messages.success(request, 'Thank you, account created. Please login')

    else:
        form = RegisForm()

    context = {'form' : form}

    return render(request, 'register.html', context=context)