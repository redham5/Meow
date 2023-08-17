from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'main/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')

def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')

def term_of_use(request):
    return render(request, 'main/term_of_use.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'main/signup.html', {
        'form' : form
    })