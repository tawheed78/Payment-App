from django.shortcuts import render
from .utils import initiate_payment, client, fetch_current_time
import razorpay
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from django.contrib.auth.decorators import login_required
from .models import verify_token, create_logs, fetch_transaction_by_order_id
from django.shortcuts import render


@login_required
@csrf_exempt
def home_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_gateway = request.POST.get('payment_gateway')
        context = {
            'amount': amount,
            'payment_gateway': payment_gateway
        }
        
    return render(request, 'home.html')     

@csrf_exempt
def razorpay_payment_view(request):
    user = request.user
    payment_gateway = 'Razorpay'
    if not user.is_authenticated:
        error_message = "User not authenticated. Please log in."
        return render(request, 'payment_failure.html', {'error': error_message})

    username = user.username
    email = user.email
    phone_number = getattr(user, 'phone_number', None)
    try:
        amount = int(request.POST.get('amount'))
        if amount <= 0:
            raise ValueError("Invalid amount")
    except (ValueError, TypeError):
        error_message = "Invalid payment amount. Please try again."
        return render(request, 'payment_failure.html', {'error': error_message})
    
    token = request.POST.get('razorpay_auth_token')
    if not token:
        error_message = "Payment token missing. Please login again."
        return render(request, 'payment_failure.html', {'error': error_message})
    token_owner = verify_token(token)
    if not token_owner['username'] == username:
        error_message = "Token verification failed. Invalid token. Please login again."
        return render(request, 'payment_failure.html', {'error': error_message})
    try:
        order_id = initiate_payment(amount)
        create_logs(order_id, amount, payment_gateway, timestamp = fetch_current_time() , status='Initiated')
    except Exception as e:
        error_message = f"Payment initiation failed: {str(e)}"
        return render(request, 'payment_failure.html', {'error': error_message})

    context = {
        'order_id': order_id,
        'amount': amount,
        'user': username,
        'email': email,
        'phone_number': phone_number,
        'token': token
    }
    return render(request, 'razorpay_payment.html', context)


@csrf_exempt
def razorpay_payment_success_view(request):
    token = request.POST.get('token')
    order_id = request.POST.get('order_id')
    payment_id = request.POST.get('razorpay_payment_id')
    signature = request.POST.get('razorpay_signature')
    if not order_id or not payment_id or not signature:
        error = "Missing required Parameter"
        context = {'error': error}
        return render(request, 'payment_failure.html', context)
    
    params_dict = {
        'razorpay_order_id': order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }
    try:
        order_data = fetch_transaction_by_order_id(order_id)
        client.utility.verify_payment_signature(params_dict)
        create_logs(
            order_id,
            amount = order_data['amount'],
            payment_gateway= order_data['payment_gateway'],
            timestamp=fetch_current_time(),
            status = 'Completed'
        )
        return render(request, 'payment_success.html')
    
    except razorpay.errors.SignatureVerificationError as e:
        error = f"Signature verification failed: {str(e)}"
        context = {'error_message': error}
        create_logs(
            order_id,
            amount = order_data['amount'],
            payment_gateway= order_data['payment_gateway'],
            timestamp=fetch_current_time(),
            status = 'Failed'
        )
        return render(request, 'payment_failure.html', context)

    except Exception as e:
        error = f"An unexpected error occurred: {str(e)}"
        context = {'error_message': error}
        create_logs(
            order_id,
            amount = order_data['amount'],
            payment_gateway= order_data['payment_gateway'],
            timestamp=fetch_current_time(),
            status = 'Failed'
        )
        return render(request, 'payment_failure.html', context)
   

@csrf_exempt
def paypal_payment_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
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


# @csrf_exempt
# def stripe_checkout_view(request):
#     if request.method=='POST':
#         try:
#             # amount = request.POST.get('amount')
#             price_id = request.POST.get('price_1Pxk8AHHXJvihBBWlXkqflwx', '{{PRICE_ID}}')
#             session_url = create_checkout_session()
#             return redirect(session_url)
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})

# @csrf_exempt
# def cancel_view(request):
#     return render(request, 'cancel.html')
