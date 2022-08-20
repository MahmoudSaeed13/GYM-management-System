from django.core.mail import send_mail
from celery import shared_task
from django.core.exceptions import ValidationError
from users.models import User


@shared_task(bind=True)
def send_new_event_email(self, event_name, event_price, start_date, end_date):
    
    users = User.objects.all()
    counter = 0
    for user in users:
        if user.is_verified and not user.is_staff:

            email_body = (
                "Hi "
                + user.name.split(" ")[0]
                + ",\n"
                + f"A new event has opened and it is {event_name}\n"
                + f"Register now and get your Ticket. only for {event_price} EGP\n"
                + f"Event is being held from {start_date[0:10]} until {end_date[0:10]} in the main branch San Stefano\n"
                + "For more information: \n"
                + "http://localhost:3000 \n"
                + "http://localhost:3000/events"
            )

            try:
                send_mail(
                    subject="New Event in Gutim",
                    message= email_body,
                    from_email="settings.EMAIL_HOST_USER",
                    recipient_list=[user.email,],
                    fail_silently=False
                )
                counter += 1
            except Exception:
                raise ValidationError("Couldn't send the message to the email!")
    return f"Done! sent {counter} emails."