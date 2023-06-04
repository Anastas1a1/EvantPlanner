from django.contrib import admin
from django.urls import path
from django.urls import include
from PlannerApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),
    path('organizations/', views.organizations, name='organizations'),
    path('events/', views.event_list, name='event-list'),
    path('events/create/', views.event_create, name='event-create'),
    path('events/<int:event_id>/edit/', views.event_edit, name='event-edit'),
    path('organization/<int:organization_id>/', views.organization_profile, name='organization-profile'),
   
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/organizations/', views.OrganizationCreateView.as_view(), name='organization-create-api'),
    path('api/events/', views.EventCreateView.as_view(), name='event-create-api'),
    path('api/events/<int:event_id>/', views.EventDetailView.as_view(), name='event-detail-api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)