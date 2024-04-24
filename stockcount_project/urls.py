"""
URL configuration for stockcount_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from scount import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.stock_home, name='home'),
    path('request', views.stock_request, name='request'),
    path('stock', views.stock_main, name='stock'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('updatestockname/<int:id>', views.updatestockname, name='updatestockname'),
    path('updatequantity/<int:id>', views.updatequantity, name='updatequantity'),
    path('approve/<int:id>', views.approve, name='approve'),
    path('approveinstock/<int:id>', views.approveinstock, name='approveinstock'),
    path('reject/<int:id>', views.reject, name='reject'),
    path('delivered/<int:id>', views.delivered, name='delivered'),
    path('complete/<int:id>', views.complete, name='complete'),
    path('log', views.stock_log, name='log'),
    path('tools', views.stock_tools, name='tools'),
    path('settings', views.stock_log, name='settings'),
    path('signout', views.stock_log, name='signout'),
    path('', views.signin, name='signin'),
]
