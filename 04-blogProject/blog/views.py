from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
### bu mixen foydalanuvchi oldin saytga kirgan kirmaganligini aniqlaydi
# UserPassesTestMixin  # bu mixin foydalanuvchi faqat o'zi yozgan maqolani taxrirlay oladi
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
#createView -- yangi narsalar qo'shish uchun tayyor djangodagi view
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(ListView):
    model=Post
    template_name = 'home.html'

class BlogDetalView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name = 'post_new.html'
    fields=['title', 'body']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name = 'post_edit.html'
    fields = ['title','body']  #qaysi maydonlarni o'zgartirish kerak bo'lsa shu yerga kiritiladi

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user

    ### bu funksiya maqolaning muallifini(author) ni oladi foydalanuvchining useri bilan solishtiradi
    ### agar moskelmasa 403 Forbidin qaytariladi

