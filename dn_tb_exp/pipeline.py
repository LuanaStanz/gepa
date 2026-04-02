import os
import pandas as pd
import datetime
import time
import re
import traceback  # para capturar stack trace completo
from loadingQuestions import retrievingQuestionsPRO, retrievingQuestionsPRE  # list
from makingRequest import modelRequestLMstudio #verificar o da Tais
print("modelRequest MADE")
from verifierFileTB import verifierTB, same_question_validTB, same_question_not_validTB
print("veri TB MADE")
from verifierFileDN import verifierDN, same_questionDN
print("veri DN MADE")
from prompts.nadia.phi4_gepa import real_prompt_phi4
#from prompts.nadia.gpt120b_gepa import real_prompt_gptoss120b
#from prompts.nadia.gpt20b_gepa import real_prompt_gptoss20b
from prompts.nadia.mistral_gepa import real_prompt_mistral
#from prompts.nadia.qwen3_32b_gepa import real_prompt_qwen3_32b
from translatorFile import translation #lisp to anita translation
print("imports ok")

def log_error(message, model_name="None yet"):
    """Salva erros no arquivo error_log.txt"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sep = "-" *200
    
    log_entry = (
        f"\n{sep}"
        f"===ERROR LOG ENTRY==="
        f"...TIME...: {current_time}\n"
        f"...MODEL NAME...: {model_name}\n"
        f"...Message...: {message}\n"
        f"...Traceback...:{traceback.format_exc()}\n"
        f"{sep}\n\n"
    )

    with open("error_log.txt", "a", encoding="utf-8") as log:
        log.write(log_entry) 

def extract_proof(response_text):
    match = re.search(r"<proof>(.*?)</proof>", response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return response_text

def pipeline(model_name, method, question_type, prompt_types_list, prompt_language=None): 
    """
    model_name: nome do modelo (ex: 'gpt-oss-20b')
    method: "tableau" or "dn"
    question_type: 'PRO' ou 'PRE'
    prompt_types_list: lista de nomes de templates/prompts
    """
    print("Starting pipeline")
    pipeline_start = time.time() 
    if "/" in model_name:
        model_name_t = model_name.replace("/", "_")
    else:
        model_name_t = model_name

    if "phi-4" in model_name:
        real_prompt_func = real_prompt_phi4
    if "mistral" in model_name:
        real_prompt_func = real_prompt_mistral
    #if "gpt-oss-20b" in model_name:
    #    real_prompt_func = real_prompt_gptoss20b
    #if "gpt-oss-120b" in model_name:
    #    real_prompt_func = real_prompt_gptoss120b
    #if "qwen3-32b" in model_name:
    #    real_prompt_func = real_prompt_qwen3_32b

    print(f"Tipos de prompts carregados: {prompt_types_list}")

    #(1)____________Carregar Questões (PRO e PRE)________________

    try:
        if question_type == "PRO":
            print("Retrieving propositional questions...")
            questions = retrievingQuestionsPRO()
        elif question_type == "PRE":
            print("Retrieving predicate questions...")
            questions = retrievingQuestionsPRE()
        else:
            msg = f"Type of questions unknow: {question_type}"
            print(msg)
            log_error(model_name, msg)
            return
    except Exception as e:
        msg = f"[PIPELINE] ERRO ao carregar questões {question_type}: {type(e).__name__} - {e}\n{traceback.format_exc()}"
        print(msg)
        log_error(msg, model_name)
        return

    print("Perguntas carregadas:", questions)

    #(2)__________verificador e prompt correto___________________
    try:
        if method.lower() == "tableau": 
            verifier_function = verifierTB    
            correct_verifier_text = "The proof is valid." #tb
            conversa_teste = [
                {"role": "system", "content": "You will be given one propositional logic theorem. Your task: generate its proof using the analytical tableau method. Output must contain ONLY the analytical tableau proof in the exact notation described below. No explanations, no comments, no extra text."},
                {"role": "user", "content": "Generate proof for '(A->B)&(~A->B) |- B' using the analytical tableau method. Fitch-like notation without comments, explanations, justifications, or additional text."}
            ]
            #same_formula_function = same_question_validTB
            #if prompt_language=="anita":
            #    real_prompt_func = real_prompt_anita 
            
        elif method.lower() == "dn":
            verifier_function = verifierDN  
            correct_verifier_text = "A demonstração está correta." #dn  
            conversa_teste = [
                {"role": "system", "content": "You will be given one propositional logic theorem. Your task: generate its proof of validity using the Natural Deduction method. Output must contain ONLY the natural deduction proof in the exact notation described below. No explanations, no comments, no extra text."},
                {"role": "user", "content": "Generate proof for '(A->B)&(~A->B) |- B' using the natural deduction method. Fitch-like notation without comments, explanations, justifications, or additional text."}
            ]
            same_formula_function = same_questionDN

            #real_prompt_func = real_prompt_nadia

        else:
            msg = f"Type is unknown: {question_type} to dn"
            print(msg)
            log_error(msg,model_name) 
            return
        
    except Exception as e:
        msg = f"[PIPELINE] ERROR in prompts/verificadores: {type(e).__name__} - {e}\n{traceback.format_exc()}"
        print(msg)
        log_error(msg, model_name)
        return

    #(3)__________loop of prompts___________________
    prompt_times_log = [] #p/ salvar tempo
    for prompt_name in prompt_types_list:
        print(f"\nRunning prompt: {prompt_name}")

        if method.lower() == "tableau": base_folder = f"results/{method}/{model_name_t}/{prompt_language}/{question_type}/{prompt_name}"
        if method.lower() == "dn": base_folder = f"results/{method}/{model_name_t}/{question_type}/{prompt_name}"
        
        os.makedirs(base_folder, exist_ok=True)
        output_filename = os.path.join(base_folder, f"results_{prompt_name}_{model_name_t}_{question_type}.csv")

    
        #(3.1)__________loop real questions with prompts padrões
        time_prompt_start = time.time()
        batch_rows = []
        batch_size = 5

        for q_index, q in enumerate(questions, start=1):
            conversa_entrada = "nenhuma conversa_entrada"
            whole_response = ""
            cut_response = ""
            finish_reason = "None"
            tokens_input = "None"
            tokens_output = "None"

            try:
                print(f"Prompt: {prompt_name}. Question: {q}") 
                conversa_entrada = real_prompt_func(question_type, prompt_name, q) 

                start_req = time.time()
                response_text, tokens_input, tokens_output, finish_reason = modelRequestLMstudio(model_name, conversa_entrada, "localhost")
                time_of_one_request = time.time() - start_req 

                whole_response = response_text
                cut_response = extract_proof(response_text)
                verification = verifier_function(cut_response) or "No string received by verifier. No string in response."
                
                if correct_verifier_text in str(verification):
                    verification = same_formula_function(verification, q)

                if "The theorem is not valid." in verification:
                    verification = same_question_not_validTB(verification, q)
                    
                print(f"Time for request of question: {round(time_of_one_request, 2)}s | finish_reason: {finish_reason}")

                batch_rows.append({
                    "question": q,
                    "input_prompt": conversa_entrada,
                    "whole_response": whole_response,
                    "cut_response": cut_response,
                    "verification": verification,
                    "time_seconds_only_request": time_of_one_request,
                    "finish_reason": finish_reason,
                    "tokens_input": tokens_input,
                    "tokens_in_output": tokens_output,
                    "translation": None    
                })

            except Exception as e:
                msg = f"[PIPELINE] Erro processando '{q}' no prompt '{prompt_name}': {type(e).__name__} - {e}\n{traceback.format_exc()}"
                print(msg)
                log_error(msg, model_name) 

                batch_rows.append({
                    "question": q,
                    "input_prompt": conversa_entrada,
                    "whole_response": whole_response,
                    "cut_response": cut_response,
                    "verification": f"Error: {type(e).__name__} - {e}",
                    "time_seconds_only_request": None,
                    "finish_reason": "error in pipeline",
                    "tokens_input": "None",
                    "tokens_in_output": "None",
                    "translation": None  
                })
                continue
            
            # salva batch
            if q_index % batch_size == 0:
                df_batch = pd.DataFrame(batch_rows)
                df_batch.to_csv(output_filename, mode='a', index=False, encoding='utf-8',header=not os.path.exists(output_filename))
                print(f"{len(batch_rows)} questions saved in {output_filename}")
                batch_rows = []

        #save rest
        if batch_rows:
            df_batch = pd.DataFrame(batch_rows)
            df_batch.to_csv(output_filename, mode='a', index=False, encoding='utf-8', header=not os.path.exists(output_filename))
            print(f"Last {len(batch_rows)} questions saved")


    #(5)__________save summary and time of prompt________________
        try:
            prompt_elapsed = round(time.time() - time_prompt_start, 2)
            prompt_times_log.append((prompt_name, prompt_elapsed))
            salveCSVsummary(method, model_name_t, prompt_name, output_filename, question_type, prompt_elapsed, prompt_language)

            
        except Exception as e:
            msg = f"[PIPELINE] Erro salvando summary: {e}\n{traceback.format_exc()}"
            print(msg)
            log_error(msg, model_name)

    #(6)__________save total time to run this model________________
    try:
        pipeline_total = round(time.time() - pipeline_start, 2)
        save_total_time_txt(method, model_name_t, question_type, prompt_times_log, pipeline_total)
    except Exception as e:
        msg = f"[PIPELINE] ERR ao salvar tempo total: {e}\n{traceback.format_exc()}"
        print(msg)
        log_error(msg, model_name) 

def salveCSVsummary(method, model_name_t, prompt_name, output_filename, question_type, prompt_elapsed, prompt_language = None):
    """
    Salva o resumo de verificações em CSV.

    method: "tableau" ou "dn"
    model_name_t: nome do modelo (ex: "mistral-7b")
    prompt_name: nome do template de prompt usado
    output_filename: caminho do CSV com todos os resultados individuais
    question_type: PRO ou PRE
    prompt_elapsed: tempo total gasto naquele prompt
    prompt_language: usado apenas no TABLEAU (ex: "anita", "dn")
    """
    df = pd.read_csv(output_filename)
    if 'verification' not in df.columns:
        df['verification'] = ""
    
    df['verification'] = df['verification'].astype(str)
        
    if method.lower() == "tableau":
        summary_folder = f"results/{method}/{model_name_t}/{prompt_language}/{question_type}/{prompt_name}"
        os.makedirs(summary_folder, exist_ok=True)
        summary_filename = f"{summary_folder}/summary_{prompt_name}_{model_name_t}_{prompt_language}.csv"

        counts = {
        'The following errors were found': df['verification'].str.startswith('The following errors were found').sum(),
        'The proof is valid.': df['verification'].str.startswith('The proof is valid.').sum(),
        'The theorem is not valid.': df['verification'].str.startswith('The theorem is not valid.').sum()
        }

        summary = pd.DataFrame(list(counts.items()), columns=['Type of answer', 'Count'])
        total = summary['Count'].sum()
        summary['Percentage'] = (summary['Count'] / total * 100).round(2) if total > 0 else 0.0
        
        summary.loc[len(summary)] = ["Total time in seconds", round(prompt_elapsed, 2), ""]
        summary.to_csv(summary_filename, index=False, encoding="utf-8")#salva csv
        print(f"Resumo salvo em: {summary_filename}")

    elif method.lower() == "dn":
        summary_folder = f"results/{method}/{model_name_t}/{question_type}/{prompt_name}"
        summary_filename = os.path.join(summary_folder, f"summary_{prompt_name}_{model_name_t}_{question_type}.csv")

        counts = {
            'Errors found': df['verification'].astype(str).str.startswith('Os seguintes erros foram encontrados').sum(),
            'Wrong theorem proved': df['verification'].astype(str).str.startswith('Demonstração do teorema errado').sum(),
            'Unexpected format': df['verification'].astype(str).str.startswith('Error successful output in unexpected format.').sum(),
            'Correct': df['verification'].astype(str).str.startswith('A demonstração está correta').sum()
        }
        summary = pd.DataFrame(list(counts.items()), columns=['Type of answer', 'Count'])
        total = summary['Count'].sum()
        summary['Percentage'] = (summary['Count'] / total * 100).round(2) if total > 0 else 0.0
        
        summary.loc[len(summary)] = ["Total time in seconds", round(prompt_elapsed, 2), ""]
        summary.to_csv(summary_filename, index=False, encoding="utf-8")
        print(f"Resumo salvo em: {summary_filename}")

    else:
        msg = f"[salveCSVsummary] Método inválido recebido: {method}"
        print(msg)
        log_error(msg, model_name_t) 

def save_total_time_txt(method, model_name_t, question_type, prompt_times_log, pipeline_total):
    """
    Salva arquivo texto com tempos por prompt + tempo total.
    """
    try:
        txt_path = f"results/{method}/{model_name_t}/{question_type}/tempo_total_{model_name_t}_{question_type}.txt"
        os.makedirs(os.path.dirname(txt_path), exist_ok=True)

        with open(txt_path, "a", encoding="utf-8") as f:
            f.write(f"TEMPOS DE EXECUÇÃO - MODEL: {model_name_t} | TYPE: {question_type}\n\n")
            for prompt_name, t in prompt_times_log:
                f.write(f"Prompt {prompt_name}: {t} segundos\n")
            f.write("\n-------------------------------------------------\n")
            f.write(f"Tempo TOTAL para todos os prompts: {pipeline_total} segundos\n")
        print(f"Arquivo de tempo total salvo em: {txt_path}")
    except Exception as e:
        msg = f"ERRO AO TENTAR SALVAR TEMPO: {type(e).__name__} - {e}"
        print(msg)
        log_error(msg, model_name_t) 
