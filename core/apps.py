from django.apps import AppConfig
from django.conf import settings
import os



class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        import core.models
        if settings.LOAD_MODEL_AT_STARTUP:
            from .gpt_model import LlamaModel
            global model
            module_dir = os.path.dirname(__file__)
            model_path = os.path.join(module_dir, './')
            model_file = 'Meta-Llama-3-8B-Instruct-Q4_K_M.gguf'
            model = LlamaModel(model_path, model_file)
