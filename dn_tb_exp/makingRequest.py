from openai import OpenAI

def modelRequestLMstudio(model_name, conversa_entrada, ip, port="1234"):
    """
    Faz requisição a um modelo local do LM Studio usando apenas chat.completions.
    conversa_entrada: lista no formato [{"role": "system", "content": ...}, {"role": "user", "content": ...}]
    """
    try:
        base_url= f"http://{ip}:{port}/v1/"
        client = OpenAI(base_url=base_url, api_key="lmstudio")
        print(f"Sending request on LM Studio to the model: {model_name} via chat.completions...")

        completion = client.chat.completions.create(
            model=model_name,
            messages=conversa_entrada,
            temperature=0,
            max_tokens=32000,
            stream=False
        )

        response = completion.choices[0].message.content
        finish_reason = completion.choices[0].finish_reason
        input_tokens = getattr(completion.usage, "prompt_tokens", None)
        output_tokens = getattr(completion.usage, "completion_tokens", None)

        print("Request succeeded using chat.completions.\n")

    except Exception as e:
        print("[REQUEST ERRO]"*100)
        print(f"\nPlease ensure LM Studio server is running and accessible at http://{ip}:{port}. Also verify the model '{model_name}' is available locally.")
        response = f"Error Type: {type(e).__name__}. ERRO: {e}"
        input_tokens = None
        output_tokens = None
        finish_reason = "error"

    return response, input_tokens, output_tokens, finish_reason
