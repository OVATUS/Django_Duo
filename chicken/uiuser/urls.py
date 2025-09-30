from django.urls import path
from .views import *

urlpatterns = [
    # User Authentication URLs
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
>>>>>>> 2b6a10c (ทำหน้เา html ทั้งหมด)
]
