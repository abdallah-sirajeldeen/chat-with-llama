from llama_cpp import Llama
import torch
import transformers

from transformers import LlamaForCausalLM, LlamaTokenizer
from ctransformers import AutoModelForCausalLM
llm = AutoModelForCausalLM.from_pretrained("TheBloke/OpenHermes-2.5-Mistral-7B-GGUF", model_file="openhermes-2.5-mistral-7b.Q2_K.gguf")
print(llm("AI is going to"))

class LlamaModel:
    def __init__(self, model_path, model_file):
        # Initialize the Llama model from a given model path
        self.model = AutoModelForCausalLM.from_pretrained(model_path,
                                             model_file=model_file)
        # self.tokenizer = LlamaTokenizer.from_pretrained(model_path)
        # AutoModelForCausalLM.from_pretrained("TheBloke/OpenHermes-2.5-Mistral-7B-GGUF",
        #                                      model_file="openhermes-2.5-mistral-7b.Q2_K.gguf")
        # self.model.eval()  # If model has an eval mode, uncomment this line

    def predict(self, input_text):
        out_put = self.model(input_text)
        return out_put
        # pipeline = transformers.pipeline(
        #     "text-generation",
        #
        #     model=self.model,
        #
        #     tokenizer=self.tokenizer,
        #
        #     torch_dtype=torch.float16,
        #
        #     device_map="auto",
        #
        # )
        # sequences = pipeline(
        #     input_text,
        #
        #     do_sample=True,
        #
        #     top_k=10,
        #
        #     num_return_sequences=1,
        #
        #     eos_token_id=self.tokenizer.eos_token_id,
        #
        #     max_length=400,
        #
        # )
        #
        # for seq in sequences:
        #     return seq['generated_text']


        # print(f"{seq['generated_text']}")
        # # Directly pass input_text to the model's prediction function/method
        # # Assume the model's method handles the text input appropriately
        # output = self.model(
        #     input_text,
        #     max_tokens=50,  # Example: limit the response to 50 tokens; adjust as needed
        #     stop=["\n"],  # Example: stop generation at newline; adjust as needed
        #     echo=True  # Echo the input text in the output; adjust as needed
        # )
        # return output
