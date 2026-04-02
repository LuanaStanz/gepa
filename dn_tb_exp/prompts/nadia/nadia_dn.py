from prompts.nadia.exemplos_nadia import exemplos_pro_nadia, exemplos_pre_nadia
from prompts.nadia.prompt_nadia import simple_pro_content, complet_pro_content, ending_pro_content, simple_pre_content, complet_pre_content, ending_pre_content
#todas regras: complet_pro_content+complet_pre_content

def real_prompt_nadia(tipo_questao, tipo_prompt, q):
    if tipo_questao == "PRO":
        exemplos = exemplos_pro_nadia
        system_prompt_simples_nadia = simple_pro_content + ending_pro_content
        system_prompt_completo_nadia = simple_pro_content + complet_pro_content + ending_pro_content
    if tipo_questao == "PRE":
        exemplos = exemplos_pre_nadia
        system_prompt_simples_nadia = simple_pre_content + ending_pre_content
        system_prompt_completo_nadia = simple_pre_content + complet_pro_content + complet_pre_content + ending_pre_content

    if tipo_prompt == 'zero_simples':
        return [
            {"role": "system", "content": system_prompt_simples_nadia},
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'zero_completo':
        return [
            {"role": "system", "content": system_prompt_completo_nadia},
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
        
    elif tipo_prompt == 'few1_simples':
        exemplo = exemplos[0]
        return [
            {"role": "system", "content": system_prompt_simples_nadia},
            {"role": "user", "content": exemplo["user"]},
            {"role": "assistant", "content": exemplo["assistant"]},
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few1_completo':
        exemplo = exemplos[0]
        return [
            {"role": "system", "content": system_prompt_completo_nadia},
            {"role": "user", "content": exemplo["user"]},
            {"role": "assistant", "content": exemplo["assistant"]},
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    
    elif tipo_prompt == 'few2_simples':
        exemplos_messages = [
            item
            for exemplo in exemplos[:2]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_simples_nadia}] + exemplos_messages + [
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few2_completo':
        exemplos_messages = [
            item
            for exemplo in exemplos[:2]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_completo_nadia}] + exemplos_messages + [
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    
    elif tipo_prompt == 'few3_simples':
        exemplos_messages = [
            item
            for exemplo in exemplos[:3]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_simples_nadia}] + exemplos_messages + [
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few3_completo':
        exemplos_messages = [
            item
            for exemplo in exemplos[:3]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_completo_nadia}] + exemplos_messages + [
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few_simples':
        exemplos_messages = [
            item
            for exemplo in exemplos[:5]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_simples_nadia}] + exemplos_messages + [
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]

    elif tipo_prompt == 'few_completo':
        exemplos_messages = [
            item
            for exemplo in exemplos[:5]
            for item in (
                {"role": "user", "content": exemplo["user"]},
                {"role": "assistant", "content": exemplo["assistant"]}
            )
        ]
        return [{"role": "system", "content": system_prompt_completo_nadia}] + exemplos_messages + [
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    else:
        raise ValueError("Tipo de prompt inválido")