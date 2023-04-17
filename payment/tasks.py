from io import BytesIO

import weasyprint
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from orders.models import Order


@shared_task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully paid.
    """
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = f"My Shop - Invoice no. {order_id}"
    message = "Please, find attached invoice for your recent purchase."
    email = EmailMessage(subject, message, "admin@myshop.com", [order.email])
    # generate PDF
    html = render_to_string("orders/order_pdf.html", {"order": order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # Attach PDF file
    email.attach(
        f"order_{order.stripe_id}.pdf", out.getvalue(), "application/pdf"
    )
    # send email
    email.send()
