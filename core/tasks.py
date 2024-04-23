from assessment.celery import app


from django.http import JsonResponse
from core.gpt_model import GGUFModel

# Initialize the model (consider doing this in a suitable place such as app initialization)
model = GGUFModel('Meta-Llama-3-8B-Instruct-Q4_K_M.gguf')


@app.task
def get_prediction(request):
    input_text = request.GET.get('input', '')
    output = model.predict(input_text)
    return JsonResponse({'response': output.tolist()})  # Adjust the output formatting as needed
