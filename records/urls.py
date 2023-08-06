from django.urls import path
from . import views
app_name = "records"

urlpatterns = [
    path('',views.home,name="home" ),
    path('login',views.login_page,name="login"),
    path('logout/',views.log_out,name="logout"),
    path('register/',views.registration,name="register"),
    path('add-record/',views.add_record,name="add-record"),
    path('update/<int:pk>',views.update_record,name="update"),
    path('delete/<int:pk>',views.delete_record,name="delete"),
    path('<int:pk>/',views.record_view,name="record-view"),
]
