from django.urls import path

from demo_app import views

urlpatterns = [
    path('',views.home,name='today'),
    path('newindex',views.newindex,name='newindex'),
    path('index',views.index,name='index'),
    path('today2',views.today2,name='today2'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('login_view',views.login_view,name='login_view'),
    path('hello_view',views.hello_view,name='hello_view'),
    path('officer_reg',views.officer_reg,name='officer_reg'),

    ]