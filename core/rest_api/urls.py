from django.urls import path, include
from . import views
from rest_framework import routers      # routers will take care of generating urls

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('programmer', views.ProgrammerView)

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', include(router.urls)),
    path('say_hello/', views.say_hello),
    path('get_data/', views.get_data),
]