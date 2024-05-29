"""Note_Taking_Application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Note_taking_app import views as r

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', r.index, name="index"),
    path('about/', r.about, name="about"),
    path('customer/', r.customer, name="customer"),
    path('customer_regpage/', r.customer_regpage, name="customer_regpage"),
    path('customer_reg/', r.customer_reg, name="customer_reg"),
    path('customer_login/', r.customer_login, name="customer_login"),
    path('logout/', r.logout, name="logout"),
    path('customer_details_display/', r.customer_details_display, name="customer_details_display"),
    path('customer_password/', r.customer_password, name="customer_password"),
    path('customer_details_edit/<str:email>', r.customer_details_edit, name="customer_details_edit"),
    path('customer_delete/<str:email>', r.customer_delete, name="customer_delete"),
    path('admin_delete/<str:email>', r.admin_delete, name="admin_delete"),
    path('customer_details_update/', r.customer_details_update, name="customer_details_update"),
    path('blog/', r.blog, name="blog"),
    path('admin_log/', r.admin_log, name="admin_log"),
    path('admin_profile/', r.admin_profile, name="admin_profile"),
    path('customer_profile/', r.customer_profile, name="customer_profile"),
    path('admin_password/', r.admin_password, name="admin_password"),
    path('admin_logout/', r.admin_logout, name="admin_logout"),
    path('admin_customer/', r.admin_customer, name="admin_customer"),
    path('display_blog/', r.display_blog, name="display_blog"),
    path('blog_update/', r.blog_update, name="blog_update"),
    path('admin_notes/', r.admin_notes, name="admin_notes"),
    path('blog_edit/<int:id>', r.blog_edit, name="blog_edit"),
    path('blog_delete/<int:id>', r.blog_delete, name="blog_delete"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

