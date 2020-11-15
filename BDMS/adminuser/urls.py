
from django.urls import path
from . import views
urlpatterns = [
    path('adminlogin/',views.admin_login,name="adminlogin"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout"),
    path('adddonar/',views.add_donar,name="adddonar"),
    path('donarlist/',views.donar_list,name="donarlist"),
    path('deletedonar/<int:id>/',views.delete_donar,name="deletedonar"),
    path('querylist/',views.query_list,name="querylist"),
    path('deletequery/<int:id>/',views.delete_query,name="deletequery"),
    path('changepass/',views.admin_change_pass,name="changepass"),
    path('updatecontactus/',views.update_contact,name="updatecontactus"),
    path('newcontactdetails/',views.new_contact_details,name="newcontactdetails"),
    path('updateaboutus/',views.update_about_us,name="updateaboutus"),
    path('newaboutdetails/',views.new_about_details,name="newaboutdetails"),


]