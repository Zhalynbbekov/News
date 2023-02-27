from django.urls import path

from . import views

# router = routers.DefaultRouter()
# router.register(r'register', views.RegisterViews)
# router.register(r'login', views.LoginViews)
# router.register(r'home', views.HomeViews)

# urlpatterns = [
#     # path('', views.main_page, name='register'),
#     # path('login/', views.login, name='login_page'),
#     # path('login/home/', views.home, name='home_page'),
#     # path('login/home/admin', views.admin, name='admin_page'),
#     path('', views.RegisterViews.as_view({'get': 'list'})),
#     path('login/', views.LoginViews.as_view({'get': 'list'})),
#     path('home/', views.HomeViews.as_view({'get': 'list'})),
# ]

urlpatterns = [
    path('login/', views.LoginViews.as_view({'post': 'create'}), name='login_page'),
    path('register/', views.RegisterViews.as_view({'post': 'create'}), name='register'),
    path('home/', views.HomeViews.as_view({'get': 'list'}), name='home'),
]
