from assessment.celery import app
#
# from django.http import JsonResponse
# from core.apps import model
#
#
# # Initialize the model (consider doing this in a suitable place such as app initialization)
#
#
# @app.task
# def get_prediction(input_text):
#     # input_text = request.GET.get('input', '')
#
#     output = model.predict(input_text)
#     return JsonResponse({'response': output.tolist()})  # Adjust the output formatting as needed
