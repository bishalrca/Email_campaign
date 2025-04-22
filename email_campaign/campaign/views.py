from django.views.generic import TemplateView, ListView, View, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import EmailList, Subscriber, Campaign
from .utility import send_campaign_emails
from django.views.generic.edit import DeleteView


class HomeView(TemplateView):
    template_name = 'campaign/home.html'


class EmailListView(View):
    def get(self, request):
        email_lists = EmailList.objects.all()
        return render(request, 'campaign/email_lists.html', {'email_lists': email_lists})

    def post(self, request):
        name = request.POST.get('name')
        EmailList.objects.create(name=name)
        return redirect('email_lists')
    
class DeleteEmailListView(DeleteView):
    model = EmailList
    success_url = reverse_lazy('email_lists')
    template_name = 'campaign/confirm_delete.html'    


class SubscriberView(View):
    def get(self, request, list_id):
        email_list = get_object_or_404(EmailList, pk=list_id)
        return render(request, 'campaign/subscribers.html', {'email_list': email_list})

    def post(self, request, list_id):
        email_list = get_object_or_404(EmailList, pk=list_id)
        email = request.POST.get('email')
        Subscriber.objects.create(email=email, email_list=email_list)
        return redirect('subscribers', list_id=list_id)
    
class DeleteSubscriberView(DeleteView):
    model = Subscriber
    template_name = 'campaign/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('subscribers', kwargs={'list_id': self.object.email_list.id})    


class CampaignListView(View):
    def get(self, request):
        campaigns = Campaign.objects.all()
        email_lists = EmailList.objects.all()
        return render(request, 'campaign/campaigns.html', {
            'campaigns': campaigns,
            'email_lists': email_lists
        })

    def post(self, request):
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_list_id = request.POST.get('email_list')

        if email_list_id == 'all':
            email_list = None  
        else:
            email_list = get_object_or_404(EmailList, pk=email_list_id)

        Campaign.objects.create(subject=subject, message=message, email_list=email_list)
        return redirect('campaigns')


class SendCampaignView(View):
    def get(self, request, campaign_id):
        campaign = get_object_or_404(Campaign, pk=campaign_id)
        send_campaign_emails(campaign)
        return redirect('campaigns')

class DeleteCampaignView(DeleteView):
    model = Campaign
    success_url = reverse_lazy('campaigns')
    template_name = 'campaign/confirm_delete.html'
