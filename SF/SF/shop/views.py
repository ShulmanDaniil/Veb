from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from django.shortcuts import render

from .models import Product, OrderItem


class ProductListView(ListView):
    template_name = 'shop/shop.html'
    model = Product
    paginate_by = 3


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'shop/shop-single.html'
    model = Product
    login_url = '/login/'


class CartListView(LoginRequiredMixin, ListView):
    model = OrderItem
    template_name = 'shop/cart.html'


    def get_queryset(self):
        return self.model.objects.filter(order__is_paid=False)
