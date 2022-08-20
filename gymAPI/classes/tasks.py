from django.core.mail import send_mail
from celery import shared_task
from django.core.exceptions import ValidationError
from users.models import User


@shared_task(bind=True)
def send_new_class_email(self, class_name, class_price):
    
    users = User.objects.all()
    counter = 0
    for user in users:
        if user.is_verified and not user.is_staff:

            email_body = (
                "Hi "
                + user.name.split(" ")[0]
                + ",\n"
                + f"A new class has opened and it is {class_name}\n"
                + f"Register now and get ready for some real training. only for {class_price} EGP\n"
                + "For more information: \n"
                + "http://localhost:3000 \n"
                + "http://localhost:3000/classes"
            )

            try:
                send_mail(
                    subject="New Class in Gutim",
                    message= email_body,
                    from_email="settings.EMAIL_HOST_USER",
                    recipient_list=[user.email,],
                    fail_silently=False
                )
                counter += 1
            except Exception:
                raise ValidationError("Couldn't send the message to the email!")
    return f"Done! sent {counter} emails."