from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views import generic
from django.contrib.auth.models import User
import os
from django.contrib.auth.views import LogoutView  # import the logout view
# Create your views here.


def index(request):
    return render(request, 'index.html')

# register user using class


class register(generic.CreateView):
    form_class = regform
    template_name = 'register.html'
    success_url = reverse_lazy('login')

# login user using class


class login(generic.View):
    form_class = logform
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = logform(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pword = form.cleaned_data['password']
                b = User.objects.all()
                for i in b:
                    if i.username == uname and i.password == pword:
                        return render(request, 'home.html', {'uname': uname})
                else:
                    return HttpResponse('Invalid Credentials')
            return HttpResponse('invalid')


class addbook(generic.CreateView):
    form_class = bookform
    template_name = 'addbook.html'
    success_url = reverse_lazy('addbook')

    def get(self, request):
        a = book.objects.all()
        image = []
        name = []
        author = []
        pdf = []
        id1 = []
        date = []
        for i in a:
            img = str(i.image).split('/')[-1]
            image.append(img)
            name.append(i.bookname)
            author.append(i.author)
            pd = str(i.pdf).split('/')[-1]
            pdf.append(pd)
            id1.append(i.id)
            date.append(i.date)
        mylist = zip(id1, name, author, image, pdf, date)
        return render(request, 'addbook.html', {'mylist': mylist})


class deletebook(generic.DeleteView):
    model = book
    template_name = 'deletebook.html'
    success_url = reverse_lazy('addbook')


class updatebook(generic.UpdateView):
    model = book
    form_class = bookform
    template_name = 'updatebook.html'
    fields = '[bookname,author,pdf,image,date]'

    def get(self, request, **kwargs):
        id1 = kwargs.get('pk')
        a = self.model.objects.get(id=id1)
        bookname = a.bookname
        author = a.author
        img = str(a.image).split('/')[-1]
        pd = str(a.pdf).split('/')[-1]
        return render(request, 'updatebook.html', {'img': img, 'pd': pd, 'bookname': bookname, 'author': author})

    def post(self, request, **kwargs):
        id1 = kwargs.get('pk')
        a = self.model.objects.get(id=id1)
        if request.method == 'POST':
            if len(request.FILES) != 0:
                if len(a.image) > 0:
                    os.remove(a.image.path)
                a.image = request.FILES['image']
                if len(a.pdf) > 0:
                    os.remove(a.pdf.path)
                a.pdf = request.FILES['pdf']
            a.bookname = request.POST.get('bookname')
            a.author = request.POST.get('author')
            a.save()
            return redirect('http://127.0.0.1:8000/addbook/')


class download(generic.CreateView):
    model = book
    template_name = 'download.html'

    def get(self, request):
        a = book.objects.all()
        name = []
        pdf = []
        for i in a:
            name.append(i.bookname)
            pd = str(i.pdf).split('/')[-1]
            pdf.append(pd)
        mylist = zip(name, pdf)
        return render(request, 'download.html', {'mylist': mylist})

# logout view - to create a logout view in class based django you can use the built in logout view
# provided by django


class customlogoutview(LogoutView):
    next_page = reverse_lazy('index')
