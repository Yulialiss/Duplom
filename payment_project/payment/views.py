from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CardPaymentForm
from .models import Transaction


def payment_view(request):
    if request.method == 'POST':
        form = CardPaymentForm(request.POST)
        if form.is_valid():
            Transaction.objects.create(
                payment_method='Card',
                card_number=form.cleaned_data['card_number'],
                card_holder=form.cleaned_data['card_holder'],
                amount=form.cleaned_data['amount']
            )
            return JsonResponse({'success': True, 'message': 'Payment Successful!'})
        return JsonResponse({'success': False, 'errors': form.errors})

    form = CardPaymentForm()
    return render(request, 'payment/payment_form.html', {'form': form})
