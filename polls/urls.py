from django.urls import path, re_path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.CafeMenuListView.as_view(), name='menu'),
    
    # path("", views.cafe_menu, name="cafe_menu"),
    # # path("ph/", views.PurchaseHistory, name="purchase_history"),
    # # ex: /polls/5/
    path("<int:pk>/menu", views.CafeMenuDetailView.as_view(), name="detail_menu"),
    # # re_path(r'(?P<menu_id>[\w\s]+)/menu/$', views.detail_cafe_menu, name='detail_cafe_menu'),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]