from django.urls import path
from meal.views import Index, CreateMeal, EditMeal, DeleteMeal, daily_summary, MealDownload, search_by_date

app_name = 'meal'

urlpatterns = [
    path('', Index.as_view(), name='home'),

    path('search/', search_by_date, name='search_meal'),

    path('download_csv/', MealDownload.as_view(), name='download_csv'),

    path('create/', CreateMeal.as_view(), name='create_meal'),

    path('edit/<int:pk>/', EditMeal.as_view(), name='edit_meal'),

    path('delete/<int:pk>/', DeleteMeal.as_view(), name='delete_meal'),

    path('daily_summary/', daily_summary, name='daily_summary'),
]