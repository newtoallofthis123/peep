from ..format import *

class Ai:
    def __init__(self, key):
        self.key = key
    def ask(self, prompt):
        import openai
        openai.api_key = self.key
        model_engine = "text-curie-001"
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        result = completion["choices"][0]
        c_print(f"OpenAI Response: {result['text']}", code="success")
        return result["text"]