from pipeline import pipeline  #source logic_team/bin/activate
import requests
import lmstudio as lms
print("no arq main")

def unload_model(model_name):
    try:
        response = requests.post(
            "http://localhost:1234/v1/models/unload",
            json={"model": model_name}
        )

        if response.status_code == 200:
            print(f"Modelo {model_name} descarregado com sucesso.")
        else:
            print(f"Erro ao descarregar: {response.text}")

    except Exception as e:
        print(f"Erro na requisição de unload: {e}")

#pipeline(model_name, method, question_type, prompt_types_list, prompt_language=None): 
def main():
    #prompt_languages = ["anita", "anita_junt", "anita_sep"]
    model_list = ["mistral-small-3.2-24b-instruct-2506"]#"phi-4"]#"gpt-oss-120b", "gpt-oss-20b", "mistral-small-3.2-24b-instruct-2506", "phi-4"]#"qwen3-32b"]#"gpt-oss-120b", "mistral-small-3.2-24b-instruct-2506", "phi-4", "openai/gpt-oss-20b"] # "mistral-small-3.2-24b-instruct-2506""phi-4",  ]#"openai/gpt-oss-20b", "mistral-small-3.2-24b-instruct-2506"]#  "deepseek-r1-distill-qwen-32b"] #"gemma-3-27b-it", "deepseek-r1-distill-llama-70b", "qwen3-32b",  , "openai/gpt-oss-120b"
    #prompt_types_list_c = ['zero_completo', 'few1_completo', 'few2_completo', 'few3_completo', 'few_completo'] # 'few_completo', 'few_simples' 
    #prompt_types_list_s = ['zero_simples', 'few1_simples', 'few2_simples','few3_simples',"few_simples"]
    for model_name in model_list:
        print(f"\n===== Loading {model_name} =====")

        try:
            model = lms.llm(model_name)  # CARREGA
        except Exception as e:
            print(f"Erro ao carregar {model_name}: {e}")
            continue
        
        pipeline(model_name, "dn", "PRO", ["gepa"])
           
        print(f"===== Unloading {model_name} =====")
        unload_model(model_name)
        
        #pipeline(model_name, "dn","PRE", prompt_types_list) #
        #pipeline(model_name, "dn", "PRO", prompt_types_list) #
        #pipeline(model_name, "tableau", "PRO",  prompt_types_list, "lisp") #
        #pipeline(model_name, "tableau", "PRE", prompt_types_list, "lisp") #PROMPT DA TAIS
    
    
if __name__ == "__main__":
    main()

#JSON, TAG, NORMAL
#3(variantes de prompt)*3(linguagens)*2(tipos de questoes)*5(modelos)       (=> 12prompts)

#simplesPRO
#simplePRE= simplesPRO + regras do PRE
#complexo

#ANALYSIS
#more than one '1.'
#doesn't start with '1.'
#palavras num dicionario padrão -> p/ detectar lingua natural
