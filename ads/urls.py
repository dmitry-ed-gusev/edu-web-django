from django.urls import path

from . import views

app_name = 'ads'

urlpatterns = [

    # info view - just to proof that /cats appis working
    path('info/', views.autoview),
]
