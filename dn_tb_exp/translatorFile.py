import re

#fazer verificação da linguagem das safezones aqui
def deslocar_operacoes(expr): #ajeitar safezones
  tokens = re.findall(r'\(|\)|[^\s()]+', expr) #(or (implies A B) C) vira ['(', 'or', '(', 'implies', 'A', 'B', ')', 'C', ')']

  def parse(it):#função recursiva que percorre iterador de tokens para reconstrir a formula
      token = next(it)
      if token == '(':
        op = next(it) #seguida de operação ou variável sozinha
        if op == 'not':
          inner = parse(it)
          next(it)  # ')'
          return f"(~{inner})"
        elif op == 'or':
          left = parse(it)
          right = parse(it)
          next(it)
          return f"({left} | {right})"
        elif op == 'and':
          left = parse(it)
          right = parse(it)
          next(it) # ')'
          return f"({left} & {right})"
        elif op == 'implies':
          left = parse(it)
          right = parse(it)
          next(it) # ')'
          return f"({left} -> {right})"
        else: #parenteses desnecessarios ex: (A)
          return op
      else: #caso base não encontra '(' só uma variável
        return token

  return parse(iter(tokens))

def traduzir_safezones(formula):
  padrao = r':formula\s*(.*?)\s*:((?:from))'
  def repl(m):
    traduzido = deslocar_operacoes(m.group(1))
    return f":formula {traduzido} :{m.group(2)}"
  return re.sub(padrao, repl, formula) #substituir partes com padrao

def mapear_brachs(expressao):
  #tirar tudo antes de (:line 1
  ind = expressao.find('1.')
  if ind != -1:
      expressao = expressao[ind:]
  #tirar ultimo parenteses e o que vinher depois dele
  index = expressao.rfind(')')
  if index != -1:
      expressao = expressao[:index]

  # substituir branch  (:line 5 por 5. {
  expressao = re.sub(r'\(:branch\s*(\d+).', r'\1. {', expressao)
  expressao = expressao.replace(')','}')
  return expressao

def ajeitar_zones(expressao): #ajeitar as zones
  # tirar todos parenteses exceto os entre :formula e :from
  def marcar_safezone(match):
    return match.group(0).replace("(", "[[PAREN_OPEN]]").replace(")", "[[PAREN_CLOSE]]")
  expressao = re.sub(r':formula\s+(.*?)(?=\s+:(?:from))', marcar_safezone, expressao, flags=re.DOTALL)

  #tirar excesso de  '(' e ')'
  expressao = re.sub(r'\(\s*:line\s*(\d+)', r'\1.', expressao)
  expressao = re.sub(r':conclusion\s*\)', 'conclusion', expressao)
  expressao = re.sub(r':from\s*(\d+)\s*\)', r' \1', expressao)
  expressao = re.sub(r':lines\s*\(\s*(\d+)\s+(\d+)\s*\)\s*\)', r'\1,\2', expressao) # :lines (_ _) para :lines _,_
  expressao = re.sub(r':premise\s*\)', 'pre', expressao)

  #continuar ajeitando
  expressao = re.sub(r':from(\d+)',r'\1', expressao)
  expressao = expressao.replace(':from','')
  expressao = expressao.replace(':status','')
  expressao = expressao.replace(':closed','@')
  expressao = expressao.replace(':formula','')

  expressao = mapear_brachs(expressao) #mapear parenteses para substituir o branch e feicha-lo direito
  expressao = expressao.replace("[[PAREN_OPEN]]", "(").replace("[[PAREN_CLOSE]]", ")")# restaurar safezones

  return expressao

def translation(formula):
  # Remove linhas que são vazias ou só têm espaços
  formula = "\n".join([linha for linha in formula.splitlines() if linha.strip() != ""])

  formula = formula.replace(";;;;", "#") #comentários
  formula = formula.replace(";;;", "#") #comentários
  formula = formula.replace(";;", "#") #comentários
  formula = formula.replace(";", "#") #comentários

  formula = traduzir_safezones(formula)
  formula = ajeitar_zones(formula) #protege parenteses do safezone, fecha branch corretamente, retira :line, :from; ajeita :conclusion, :premise, :lines

  return formula

