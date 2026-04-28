from llama_cpp import Llama


llm = Llama(
    model_path="./llm/model.gguf",
    n_ctx=2048,
    n_threads=8,
    verbose=False,
    stream=True
)


def generate_stream(prompt: str):
    for chunk in llm(
        prompt,
        max_tokens=256,
        temperature=0.7,
        stop=["</s>"]
    ):
        yield chunk["choices"][0]["text"]