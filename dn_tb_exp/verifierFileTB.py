from anita.anita_en_fo import check_proof #pip install anita

from anita.anita_en_fo import check_proof
import re
def verifierTB(proof):
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

def normalize(s):
    s = s.replace("⊢", "|-")
    s = re.sub(r"[\s\(\)]", "", s) #tira espaços, tabs, quebras de linha e parênteses
    return s
        
def same_question_validTB(verification, q):
    if "The proof is valid." in verification:
        formula_provada = verification.split("The proof is valid.")[1].strip()
        formula_provada = re.split(r"Latex:", formula_provada)[0].strip()
    else:
        return "Error successful output in unexpected format."

    if normalize(formula_provada) != normalize(q):
        return f"Demonstração do teorema errado. A fórmula provada foi: {formula_provada}, porém deveria ser: {q}."

    return "The proof is valid."

def same_question_not_validTB(verification, q):
    if "The theorem is not valid." in verification:
        formula_provada = verification.split("The theorem is not valid.")[1].strip()
        formula_provada = re.split(r"Latex:", formula_provada)[0].strip()
    else:
        return "Error successful output in unexpected format."

    if normalize(formula_provada) != normalize(q):
        return f"Demonstração do teorema errado. A fórmula provada foi: {formula_provada}, porém deveria ser: {q}."

    return "The theorem is not valid."
