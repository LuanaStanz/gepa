from prompts.anita.exemplos_anita import exemplos_pro_anita, exemplos_pre_anita
from prompts.anita.prompt_anita import system_prompt_simples_anita_pro, system_prompt_completo_anita_pro, ending_pro_content, system_prompt_simples_anita_pre, system_prompt_completo_anita_pre, ending_pre_content
print("prompt anita loaded")

def real_prompt_anita(tipo_questao, tipo_prompt, q):
    if tipo_questao == "PRO":
        exemplos = exemplos_pro_anita
        system_prompt_simples_anita = system_prompt_simples_anita_pro + ending_pro_content
        system_prompt_completo_anita = system_prompt_simples_anita_pro + system_prompt_completo_anita_pro + ending_pro_content
    if tipo_questao == "PRE":
        exemplos = exemplos_pre_anita
        system_prompt_simples_anita = system_prompt_simples_anita_pre + ending_pre_content
        system_prompt_completo_anita = system_prompt_simples_anita_pre + system_prompt_completo_anita_pro + system_prompt_completo_anita_pre + ending_pre_content

    if tipo_prompt == 'zero_simples':
        return [
            {"role": "system", "content": system_prompt_simples_anita},
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'zero_completo':
        return [
            {"role": "system", "content": system_prompt_completo_anita},
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
        
    elif tipo_prompt == 'few1_simples':
        exemplo = exemplos[0]
        return [
            {"role": "system", "content": system_prompt_simples_anita},
            {"role": "user", "content": exemplo["user"]},
            {"role": "assistant", "content": exemplo["assistant"]},
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few1_completo':
        exemplo = exemplos[0]
        return [
            {"role": "system", "content": system_prompt_completo_anita},
            {"role": "user", "content": exemplo["user"]},
            {"role": "assistant", "content": exemplo["assistant"]},
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    
    elif tipo_prompt == 'few2_simples':
        exemplo = [
            item
            for exemplo in exemplos[:2]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_simples_anita}] + exemplo + [
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few2_completo':
        exemplo = [
            item
            for exemplo in exemplos[:2]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_completo_anita}] + exemplo+ [
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    
    elif tipo_prompt == 'few3_simples':
        exemplo = [
            item
            for exemplo in exemplos[:3]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_simples_anita}] + exemplo + [
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few3_completo':
        exemplo = [
            item
            for exemplo in exemplos[:3]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_completo_anita}] + exemplo + [
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few_simples':
        exemplo = [
            item
            for exemplo in exemplos[:5]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_simples_anita}] + exemplo + [
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few_completo':
        exemplo = [
            item
            for exemplo in exemplos[:5]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_completo_anita}] + exemplo + [
            {"role": "user", "content": f"Prove'{q}' using the analytical tableau method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    else:
        raise ValueError("Tipo de prompt inválido")
