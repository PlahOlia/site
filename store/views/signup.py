from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print('9')
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register()
            return redirect('store:homepage')
        else:
            print('8')
            data = {
                'error': error_message,
                'values': value
            }
            print(data)
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if customer.isExists ():
            error_message = 'Такой адрес уже существует..'
        return error_message
