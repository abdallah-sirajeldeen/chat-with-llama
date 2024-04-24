import os

from celery import Celery
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from assessment.celery import app


class LlamaModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        self.model = LlamaCpp(
            model_path=model_path,
            temperature=0.75,
            max_tokens=2000,
            top_p=1,
            verbose=True
        )

    def get_model(self):
        return self.model


# Define a top-level function for Celery
# @app.task
def predict(input_text, model_path):
    model = LlamaModel(model_path).get_model()
    print('invoke started')
    return model.invoke(input_text)


# Function to dispatch Celery task
def predict_prompt(input_text):
    module_dir = os.path.dirname(__file__).replace('core', 'gpt_models')
    model_path = os.path.join(module_dir, 'codellama-7b-python.Q2_K.gguf')
    result = predict(input_text, model_path)
    print('invoke finished')
    print(result)
    return result
