from django.urls import path
from .views import HomeView, EmailListView, SubscriberView, CampaignListView, SendCampaignView
from .views import (
    EmailListView, SubscriberView, CampaignListView, SendCampaignView,
    DeleteEmailListView, DeleteSubscriberView, DeleteCampaignView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('email-lists/', EmailListView.as_view(), name='email_lists'),
    path('email-lists/delete/<int:pk>/', DeleteEmailListView.as_view(), name='delete_email_list'),
    path('email-lists/<int:list_id>/subscribers/', SubscriberView.as_view(), name='subscribers'),
    path('campaigns/', CampaignListView.as_view(), name='campaigns'),
    path('campaigns/send/<int:campaign_id>/', SendCampaignView.as_view(), name='send_campaign'),
    path('campaigns/delete/<int:pk>/', DeleteCampaignView.as_view(), name='delete_campaign'),
    path('subscribers/delete/<int:pk>/', DeleteSubscriberView.as_view(), name='delete_subscriber'),
]

urlpatterns += [
    
    
    
]

