'''This code goes in views.py i think'''

from django.http import JsonResponse

def receive_data_from_js(request):
    if request.method == 'POST':

        # Get data from the POST request
        received_data = request.POST

        '''Logic'''
        return JsonResponse({'message:' 'Data received successfully'})
    else:

        # If the response is not POST, return an error response
        return JsonResponse({'error': 'Only POST requests are allowed'})
