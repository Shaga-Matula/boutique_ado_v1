from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NvFG2KnbYEnx5OfpEnDXH3ibrWRTB8pTuGf0njsHe3s3FCHAkz4Xh2NG2N7v84Fb6tSYDg5rHPVsUBs9rUZNnQa00XecMkKdS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
