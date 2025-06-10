from django.urls import path
from .import views

app_name = 'fetch'

urlpatterns = [
    path('', views.index_page, name='fetch_index'),

    path('random-quote/', views.random_quote, name=''),
    path('get-weather/', views.get_weather, name='get_weather'), 
    path('get-time/', views.get_time, name='get_time'), 
    path('get-public-record/', views.get_PR, name=''),
    path('add-something/', views.add_data, name=''),

    path('bookshelf/', views.bookshelf, name='bookshelf'),
    path('ajax/book/quantity/<int:book_id>/', views.check_book_quantity_js),
    path('ajax/book/stock-stream/<int:book_id>/', views.check_book_stock_sse),

]