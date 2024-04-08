from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from polls.models import Menu, MenuCategory, Order
from django.views.generic import ListView, DetailView

# Create your views here.
class CafeMenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menu_LV_obj'


class CafeMenuDetailView(DetailView):
    model = Menu
    template_name = 'polls/detail_cafe_menu.html'
    context_object_name = 'cafe_detail_obj'
    

    # def get_context_data(self, kwargs):
    #     context = super().get_context_data(kwargs)
    #     context['order_id'] = self.kwargs.get('order_id')
    #     return context


# def cafe_menu(request):
#     cafe_menu_list = Menu.objects.all()
#     context = {"cafe_menu_list": cafe_menu_list}
#     return render(request, 'menu_list.html', context)


# def PurchaseHistory(request):
#     receipt = MenuCategory.objects.all()
#     return render(request, 'purchase_history.html', {'receipt': receipt})

# # --------------------------

# def detail_cafe_menu(request, menu_id):
#     # detail_menu = get_object_or_404(MenuCategory, pk=menu_id)
#     coffee_menu = MenuCategory.objects.filter(menu = 1)
#     latte_menu = MenuCategory.objects.filter(menu = 2)
#     tea_menu = MenuCategory.objects.filter(menu = 3)
#     dessert_menu = MenuCategory.objects.filter(menu = 4)
#     context = {"coffee_menu": coffee_menu,
#                "latte_menu": latte_menu,
#                "tea_menu": tea_menu,
#                "dessert_menu": dessert_menu,}
#     return render(request, "polls/detail_cafe_menu.html", context)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     pass