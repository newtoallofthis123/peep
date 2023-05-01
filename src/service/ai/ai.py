# from ..format import *

class Ai:
    def __init__(self, key):
        self.key = key
    def ask(self, prompt):
        import openai
        openai.api_key = self.key
        model_engine = "text-davinci-003"
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
        # c_print(f"OpenAI Response: {result['text']}", code="success")
        print(result["test"])
        return result["text"]

ai = Ai(key="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")
ai.ask("print hello world in c")