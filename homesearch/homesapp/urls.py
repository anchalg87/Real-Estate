from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('buy/', views.PropertiesView.as_view(), name='buy'),
    path('buy/<int:pk>/', views.PropertyDetail.as_view(), name='prop-detail'),
    path('buy/<int:pk>/update/', views.PropertyUpdateView.as_view(), name='prop-update'),
    path('buy/<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='prop-delete'),
    path('findagent/<int:pk>/', views.AgentDetail.as_view(), name='agent-detail'),
    path('sell/', views.sellproperty, name='sell'),
    path('findagent/', views.AgentsView.as_view(), name='findagent'),
    path('contactus/', views.contactus, name='contact'),
]
