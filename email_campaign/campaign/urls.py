from django.urls import path
from .views import HomeView, EmailListView, SubscriberView, CampaignListView, SendCampaignView
from .views import (
    EmailListView, SubscriberView, CampaignListView, SendCampaignView,EditEmailListView,
    DeleteEmailListView, DeleteSubscriberView, DeleteCampaignView,EditSubscriberView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('email-lists/', EmailListView.as_view(), name='email_lists'),
    path('email-lists/delete/<int:pk>/', DeleteEmailListView.as_view(), name='delete_email_list'),
    path('email-lists/<int:list_id>/subscribers/', SubscriberView.as_view(), name='subscribers'),   
    path('email-lists/edit/<int:pk>/', EditEmailListView.as_view(), name='edit_email_list'), 
    path('campaigns/', CampaignListView.as_view(), name='campaigns'),
    path('campaigns/send/<int:campaign_id>/', SendCampaignView.as_view(), name='send_campaign'),
    path('campaigns/delete/<int:pk>/', DeleteCampaignView.as_view(), name='delete_campaign'),
    path('subscribers/delete/<int:pk>/', DeleteSubscriberView.as_view(), name='delete_subscriber'),
    path('subscribers/edit/<int:pk>/', EditSubscriberView.as_view(), name='edit_subscriber'),
]

urlpatterns += [
    
    
    
]

