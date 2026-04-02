import os

def retrievingQuestionsPRO():
    file_path = os.path.join("questions", "PRO.txt")

    questions_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                formula = line.strip()

                if formula:
                    questions_list.append(formula)

    except FileNotFoundError:
        print(f"[PRO] Arquivo não encontrado: {file_path}")
    except Exception as e:
        print(f"[PRO] Erro ao ler o arquivo {file_path}: {e}")
        return []

    return questions_list


def retrievingQuestionsPRE():
    file_path = os.path.join("questions", "PRE.txt")

    questions_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                formula = line.strip()

                if formula:
                    questions_list.append(formula)

    except FileNotFoundError:
        print(f"[PRE] Arquivo não encontrado: {file_path}")
    except Exception as e:
        print(f"[PRE] Erro ao ler o arquivo {file_path}: {e}")

    return questions_list
