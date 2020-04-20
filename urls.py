from django.urls import path
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user_reg', views.user_regView)

urlpatterns = [
    
    path('', include(router.urls)),
    path('admin/', admin.site.urls)

]

