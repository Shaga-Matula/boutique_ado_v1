from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe
from bag.contexts import bag_contents
from .forms import OrderForm






def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY



    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
    amount=stripe_total,
    currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        # 'stripe_public_key': 'pk_test_51NvFG2KnbYEnx5OfpEnDXH3ibrWRTB8pTuGf0njsHe3s3FCHAkz4Xh2NG2N7v84Fb6tSYDg5rHPVsUBs9rUZNnQa00XecMkKdS',
        # 'client_secret': 'sk_test_51NvFG2KnbYEnx5OfqOWebbmbUvnyzEAcD9Ka45GSWeFbGtiht2PLMXxinXv6gdTdLBtFLXCgELDqouRAjVu0wpwN00hDeaZrME',
    }

    return render(request, template, context)
