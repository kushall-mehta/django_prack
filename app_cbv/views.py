from django.shortcuts import render
from .models import *
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required#for decorator
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context= {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available

    }

    return render(request,'app_cbv/index.html',context=context)

class BookCreate(LoginRequiredMixin,CreateView): #model_form.html #add the view here
    model = Book
    fields = '__all__'


    # success_url =
class BookDetail(DetailView):
        model = Book
        template_name = 'app_cbv/book_details.html'
@login_required #when user logged in only then can see the page else not possible
def my_view(request):
    return render(request,'app_cbv/my_view.html')
