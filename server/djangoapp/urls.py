from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    path('', view=views.get_dealerships, name='index'),
    path('about', views.about, name='aboutus'),
    path('contact', views.contact, name='contactus'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("register", views.registration_request, name="register"),
    path('api/dealership', views.dealerships, name='dealerships'),
    path('api/state', views.dealerships3, name='dealerships3'),
    path('api/dealership?state=<str:state>', views.get_dealer_state, name='get_dealer_state'),
    path('api/dealership/<int:dealer_id>', views.get_dealer_details, name='get_dealer_details'),
    path('api/review/<int:dealer_id>', views.dealer_details, name='dealer_details'),
    path('api/addreview/<int:dealer_id>/', views.add_review, name='add_review'),


    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
