from django.urls import path
from goal.views import UpdateGoal

app_name = 'goal'

urlpatterns = [
    path('update/<int:pk>/', UpdateGoal.as_view(), name='update_goal'),
]