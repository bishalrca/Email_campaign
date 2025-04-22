from django.core.mail import send_mass_mail
from django.utils import timezone
from .models import Subscriber


def send_campaign_emails(campaign):
    if campaign.email_list is None:
        # All lists
        subscribers = Subscriber.objects.all()
    else:
        subscribers = campaign.email_list.subscriber_set.all()

    recipient_list = [s.email for s in subscribers]

    # Bulk email sending
    send_mass_mail([(campaign.subject, campaign.message, 'your@email.com', recipient_list)])

    campaign.sent_at = timezone.now()
    campaign.save()

