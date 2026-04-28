from llama_cpp import Llama


# загружаем модель один раз при старте
llm = Llama(
    model_path="./llm/model.gguf",
    n_ctx=2048,
    n_threads=8,  # под CPU
    verbose=False
)


def generate(prompt: str) -> str:
    result = llm(
        prompt,
        max_tokens=256,
        temperature=0.7,
        stop=["</s>"]
    )

    return result["choices"][0]["text"]