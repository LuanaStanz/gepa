pro_content = r"""
"""

from prompts.nadia.exemplos_nadia import exemplos_pro_nadia, exemplos_pre_nadia
from prompts.nadia.prompt_nadia import simple_pro_content, complet_pro_content, ending_pro_content, simple_pre_content, complet_pre_content, ending_pre_content
#todas regras: complet_pro_content+complet_pre_content

def real_prompt_qwen3_32b(tipo_questao,prompt_name_decorativo, q):
    if tipo_questao == "PRO":
        return [            
            {"role": "system", "content": pro_content},
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    #if tipo_questao == "PRE":
        #por enquanto nada
