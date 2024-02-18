from django.shortcuts import render
from django.http import JsonResponse
import json

# Basic view 
def receive_data_from_js(request):
    if request.method == 'POST':

        # Get data from the POST request
        received_data = json.loads(request.body.decode('utf-8'))

        # Extract the input data from the received data
        input_data = received_data.get('input_data')

        '''Logic!!!
            Here is where we'll construct 
        '''
        return JsonResponse({'message:' 'Data received successfully'})
    else:

        # If the response is not POST, return an error response
        return JsonResponse({'error': 'Only POST requests are allowed'})