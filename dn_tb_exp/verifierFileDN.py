from nadia.nadia_pt_fo import check_proof #pip install nadia-proof

def verifierDN(proof):
    try:
        result = check_proof(proof)
        if result is None:
            result = "ERRO in check_proof!!!"
        print("Verified")
        return str(result)
    except Exception as e:
        print(proof)
        print(f"Erro in the verifier: {e}")
        return f"Verifier error: {e}"

def same_questionDN(verification, q):
    '''
    Corta mensagem de sucesso do verificador
    e verifica se a fórmula provada é a questão pedida.
    Retorna o texto ajustado.
    '''
    # Remover tudo a partir de "Código da demonstração"
    if "Código da demonstração" in verification:
        verification = verification.split("Código da demonstração")[0].strip()
    else:
        verification = "Error successful output in unexpected format."
    
    # Extrair fórmula provada
    partes = verification.split("A demonstração está correta.")
    if len(partes) > 1:
        formula_provada = partes[1].strip()
    else:
        verification = "Error successful output in unexpected format."

    # Normalizar removendo todos espaços e quebras de linha
    formula_provada_normalizada = formula_provada.replace(" ", "").replace("\n", "")
    formula_questao_normalizada = q.replace(" ", "").replace("\n", "")

    # Comparar as fórmulas
    if formula_provada_normalizada != formula_questao_normalizada:
        verification = f"Demonstração do teorema errado. A fórmula provada foi: {formula_provada}, porém deveria ser: {q}."

    return verification
