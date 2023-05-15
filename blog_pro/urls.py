"""blog_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blog_app import views
urlpatterns = [
    path('login1',views.login,name='login1'),
    path("com",views.com,name="com"),
    path('comment/<int:id>',views.comment,name='comment'),
    path('deletecomment/<int:id>/<int:post_id>',views.deletecomment,name='deletecom'),
    path('about',views.about,name='about'),
    path('feed',views.feed,name='feed'),
    path('admin/', admin.site.urls),
    path('base',views.base,name='base'),
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('delete<int:id>',views.dele,name='dele'),
    path('addblog',views.addblog,name='addblog'),
    path('contact',views.contact,name='contact'),
    path('showcontact',views.showcontact,name='showcontact'),
    path('edit',views.edit,name='edit'),
    path('profile',views.profile,name='profile'),
    path('profileimage',views.profileimage,name='profileimage'),
    path('deletei<int:id>',views.deletei,name='deletei'),
    path('updatei<int:id>',views.updatei,name='updatei'),
    path('sign',views.sign,name='sign'),
    path('showsign',views.showsign,name='showsign'),
    path('delete<int:id>',views.delete,name='delete'),
    path('update1<int:id>',views.update1,name='update1'),
    path('update<int:id>',views.update,name='update'),

    path('logout',views.logout,name='logout'),
    path('change',views.change_p,name='change'),
    path('readmore<int:id>',views.readmore,name='readmore'),
    path('search',views.search,name='search'),
    path('<str:title>',views.filt,name='filt'),

]
