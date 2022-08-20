from django.core.mail import send_mail
from celery import shared_task
from django.core.exceptions import ValidationError
from users.models import User


@shared_task(bind=True)
def send_new_branch_email(self, branch_name, branch_address):
    
    users = User.objects.all()
    counter = 0
    for user in users:
        if user.is_verified and not user.is_staff:

            email_body = (
                "Hi "
                + user.name.split(" ")[0]
                + ",\n"
                + f"A new branch is opened!\n"
                + f"we got a new place so you won't miss you training where ever you are\n"
                +f"{branch_name} at the address {branch_address}\n"
                +f"We are waiting for you!\n"
                + "For more information: \n"
                + "http://localhost:3000 \n"
                + "http://localhost:3000/branches"
            )

            try:
                send_mail(
                    subject="Gutim got another branch in the family",
                    message= email_body,
                    from_email="settings.EMAIL_HOST_USER",
                    recipient_list=[user.email,],
                    fail_silently=False
                )
                counter += 1
            except Exception:
                raise ValidationError("Couldn't send the message to the email!")
    return f"Done! sent {counter} emails."