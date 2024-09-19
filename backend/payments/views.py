from django.http import JsonResponse
from django.shortcuts import redirect, render
from .utils import initiate_payment, client, create_checkout_session
import razorpay
from django.views.decorators.csrf import csrf_exempt
from decouple import config

@csrf_exempt
def home_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_gateway = request.POST.get('payment_gateway')
        context = {
            'amount': amount,
            'payment_gateway': payment_gateway
        }
        # if payment_gateway == 'Razorpay':
        #     return redirect('payment', amount=amount)
        # elif payment_gateway == 'PayPal':
        #     return redirect('paypal_payment', amount=amount)
    return render(request, 'home.html')     

@csrf_exempt
def razorpay_payment_view(request):
   amount = int(request.POST.get('amount'))  # Set the amount dynamically or based on your requirements
   order_id = initiate_payment(amount)
   context = {
       'order_id': order_id,
       'amount': amount
   }

   return render(request, 'razorpay_payment.html', context)

@csrf_exempt
def razorpay_payment_success_view(request):
   order_id = request.POST.get('order_id')
   payment_id = request.POST.get('razorpay_payment_id')
   signature = request.POST.get('razorpay_signature')
   params_dict = {
       'razorpay_order_id': order_id,
       'razorpay_payment_id': payment_id,
       'razorpay_signature': signature
   }
   try:
       client.utility.verify_payment_signature(params_dict)
       return render(request, 'payment_success.html')
   except razorpay.errors.SignatureVerificationError as e:
       return render(request, 'payment_failure.html')
   

@csrf_exempt
def paypal_payment_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        print(amount)
        client_id = config('PAYPAL_CLIENT_ID')
        context = {
                'amount': amount,
                'client_id': client_id
            }
        return render(request, 'paypal_payment.html', context)
    else:
        return render(request, 'home.html')



@csrf_exempt
def paypal_payment_success_view(request):
    return render(request, 'payment_success.html')


@csrf_exempt
def stripe_checkout_view(request):
    if request.method=='POST':
        try:
            # amount = request.POST.get('amount')
            price_id = request.POST.get('price_1Pxk8AHHXJvihBBWlXkqflwx', '{{PRICE_ID}}')
            session_url = create_checkout_session()
            return redirect(session_url)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def cancel_view(request):
    return render(request, 'cancel.html')
