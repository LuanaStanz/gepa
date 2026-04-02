simple_pro_content = r"""You are an expert in logic using the Natural Deduction method.
You will receive one propositional logic problem. Your task is to prove its validity using Natural Deduction method and represent the proof in a Fitch-like notation, following these formatting instructions.

### FORMAT OF PROOF LINES
Each proof line must be structured like: '<line_number>. <formula> <origin>'
- <line_number>: sequential integer, always ending with a dot ('1.', '2.', '3.', ...)
- <formula>: the formula derived on that line
- <origin>: either 'pre' (premise), 'hip' (hypothesis) or '<rule_name> <line_refs>'
  - <rule_name> and <line_refs>: 
    - &e (1 line)  
    - &i (2 lines)  
    - ->e (2 lines)  
    - ->i (1 range)  
    - ~e (2 lines)  
    - ~i (1 range)  
    - |e (1 line + 2 ranges)  
    - |i (1 line)  
    - @e (1 line)  
    - raa (1 range)  
    - copie (1 line)  
  - <line_refs>: Must be comma-separated line numbers or ranges. Ranges denote subproofs (e.g., `->i 8-12`, `|e 4, 5-9, 10-14`)

### SUBPROOFS / HYPOTHESES
Use subproofs for hypotheses. Use curly braces '{' and '}' to open and close subproofs. 
Place `{` immediately after the line number (e.g. '8.{ A|B hip') and `}` at the end of the final line of the subproof (e.g. '10. B @e 4}').
Nested subproofs are allowed. But a formula may only be used at a specific point if it appeared earlier in the same subproof or an outer subproof to the current subproof.

### SYMBOLS & CONVENTIONS
Use the following symbols for logical operations: 
- & = conjunction (and) 
- | = disjunction (or) 
- ~ = negation (not) 
- -> = implication (implies)
 """
complet_pro_content = r"""\n \n# General Scheme for each Natural Deduction Rule\nOnly use the natural deduction rules defined below. Don't invent new rules or shortcuts.\n\n###Initial Setup\nRemember the problem given contains premises (separated by commas) before the symbol |-, and the formula after |- is the conclusion.\n\nStep 1: Write all premises first with origin 'pre'.\n\nA proof for <premise_1>,<premise_2>, … <premise_k> ⊢ <conclusion_formula> must begin like: \n1. <premise_1> pre \n2. <premise_2> pre \n... \nn. <premise_k> pre\n...\n\nThen expand line by line using only the rules below until the <conclusion_formula> is derived.\n----------------------------------------------------------------------------------------\n### Conjunction Introduction (&i)\nIf 'D' and 'B' are true, infer D & B.\n\nScheme:\nm. D\nn. B\n...\np. D & B   &i  m,n\n\n### Conjunction Elimination (&e)\nFrom D & B, infer D or B (or both).\n\nScheme 1:\nm. D & B \n...\nn. D   &e m\n\nScheme 2:\nm. D & B \n...\np. B   &e m\n\n### Implication Introduction (->i)\nIf the hypothesizing D leads to B, infer D -> B.\n\nScheme:\nm.{D hip \n...\nn. B   }\nn+1. D -> B ->i  m-n\n\n### Implication Elimination (->e)\nFrom D -> B and D, infer B.\n\nScheme:\nm. D -> B \n...\nn. D \n...\np. B   ->e  m,n\n\n### Disjunction Introduction (|i)\nFrom D or B, infer D | B.\n\nScheme 1:\nm. D \n...\np. D | B   |i  m\n\nScheme 2:\nm. B \n...\np. D | B   |i  m\n\n### Disjunction Elimination (|e)\nFrom D | B, prove C by showing that in both of these cases C is true.\n\nScheme:\nm.  D | B \nm+1. { D hip\nn. C  }\nn+1. { B hip\np. C  }\n...\np+1. C   |e  m, (m+1)-n, (n+1)-p\n\n### Negation Introduction (~i)\nIf assuming B leads to contradiction (@), infer ~B.\n\nScheme:\nm.{B hip \n... \nn. @ }\nn+1. ~B   ~i  m-n\n\n### Negation Elimination (~e)\nFrom D and ~D, infer contradiction.\n\nScheme:\nm.  D \nn.  ~D \n...\np. @   ~e  m,n\n\n### Contradiction Elimination (@e)\n**ONLY** inside a subproof: from @ infer any formula B.\n\nScheme:\nm.  @ \n...\nn.  B   @e m\n\n### Reductio ad Absurdum (raa)\nIf assuming ~D leads to contradiction, infer D.\n\nScheme:\nm.{~D hip\n...\nn. @ }\nn+1. D   raa  m-n\n\n### Copy Rule (copie)\nDuplicate a formula at a later line if needed.\n\nScheme:\nm. D\n...\nn. D   copie m\n """

ending_pro_content = r""" Write only the final proof in <proof>...</proof> tags. Only use <proof>...</proof> tags ONCE. Only use these symbols inside the proof '&' , '->', '~', '|', '@', '(', ')', '{', '}'.
Do not include explanations, commentary, or extra text inside and outside the <proof>...</proof> tags.
 """

simple_pre_content = r"""You are an expert in logic using the Natural Deduction method.
You will receive one first order logic problem. Your task is to prove its validity using Natural Deduction method and represent the proof in a Fitch-like notation, following these formatting instructions.

### FORMAT OF PROOF LINES
Each proof line must be structured like: '<line_number>. <formula> <origin>'
- <line_number>: sequential integer, always ending with a dot ('1.', '2.', '3.', ...)
- <formula>: the formula derived on that line
- <origin>: either 'pre' (premise), 'hip' (hypothesis) or '<rule_name> <line_refs>'
  - <rule_name> and <line_refs>: 
    - &e (1 line)  
    - &i (2 lines)  
    - ->e (2 lines)  
    - ->i (1 range)  
    - ~e (2 lines)  
    - ~i (1 range)  
    - |e (1 line + 2 ranges)  
    - |i (1 line)  
    - @e (1 line)  
    - raa (1 range)  
    - copie (1 line)  
    - Ae (1 line)
    - Ai (1 range)
    - Ee (1 line + 1 range)
    - Ei (1 line)
  - <line_refs>: Must be comma-separated line numbers or ranges. Ranges denote subproofs (e.g., `->i 8-12`, `|e 4, 5-9, 10-14`)

### SUBPROOFS / HYPOTHESES
Use subproofs for hypotheses. Use curly braces '{' and '}' to open and close subproofs. 
Place `{` immediately after the line number (e.g. '8.{ A|B hip') and `}` at the end of the final line of the subproof (e.g. '10. B @e 4}').
Nested subproofs are allowed. But a formula may only be used at a specific point if it appeared earlier in the same subproof or an outer subproof to the current subproof.

### SYMBOLS & CONVENTIONS
Use the following symbols for logical operations: 
- & = conjunction (and) 
- | = disjunction (or) 
- ~ = negation (not) 
- -> = implication (implies)
- Quantifiers: Ax for ∀x ; Ex for ∃x

Atoms: uppercase letters such as P, Q, R.  
Predicates: uppercase letters with parentheses, e.g., H(x), M(y), Q(a,b).  
Variables: lowercase initial, possibly followed by letters/numbers (e.g., x, x0, xP0).  
Order of precedence: ~, ∀, ∃, &, |, ->

### TO CREATE NEW VARIABLE:
For Universal Introduction (Ai): open a subproof with a fresh variable not occurring in any open hypothesis.
Create new variable like this:  '<line_number>. { <new_variable> '

For Existential Elimination (Ee): open a subproof with a fresh witness constant/variable. 
Create new variable like this: '<line_number>. {<new_variable> φ[<old_variable>/<new_variable>] hip
 """
complet_pre_content = r"""
### Important concept for first order Concept Substitution (φ[x/t])
- φ[x/t]means: replaces ONLY the FREE occurrences of the variable x in the formula φ with the term t.
- Bound occurrences of x (those inside quantifiers such as Ax, Ex) must NOT be replaced.
- The term t must be substitutable for x in φ. A term t is substitutable for x in φ if no variable occurring in t becomes accidentally bound by a quantifier in φ after substitution.
- All variables inside t must remain free after substitution. If any variable inside t would become bound after substitution (variable capture), the substitution is illegal.
- Bound variables are never replaced.

**Examples of correct substitution:**
(Ay(P(x,y) → Ax M(x)))[x/a] = Ay(P(a,y) → Ax M(x))
(the x inside Ax M(x) is bound, so it stays unchanged)

(Ay(P(x,y) → M(x)))[x/a] = Ay(P(a,y) → M(a))
(the variable a is substitutable for x, since a contains no variables nothing can become bound)

**Example of illegal substitution:**
y is NOT substitutable for x in: Ay(P(x,y) → M(y))
Because performing φ[x/y] gives: Ay(P(y,y) → M(y))
Here, the substituted y becomes bound by ∀y, which changes the meaning of the formula.  
This is variable capture, so substitution is forbidden.

### FIRST-ORDER LOGIC NATURAL DEDUCTION RULES
###Rule of Universal Elimination (Ae)
- Previously:
m. Ax φ
- Demonstration of general application of the rule:
n. φ[x/t] Ae m

###Rule of Existential Introduction (Ei)
- Previously:
m. φ[x/t]
- Demonstration of general application of the rule:
p. Ex φ Ei m

###Rule of Universal Introduction (Ai)
Note: 'a' being a new variable is mandatory.
- Previously:
m. { a
...
n.   M(a) }
- Demonstration of general application of the rule:
n+1. Ax M(x) Ai m-n

###Rule of Existential Elimination (Ee)
Note: 'a' being a new variable is mandatory.
- Previously:
m. Ex φ
n. {a φ[x/a] hip
...
p.  @ }
- Demonstration of general application of the rule:
p+1. @ Ee m, n-p 
"""
ending_pre_content = r""" Write only the final proof in <proof>...</proof> tags. Only use <proof>...</proof> tags ONCE. Only use these symbols inside the proof '&' , '->', '~', '|', '@', '(', ')', '{', '}', 'Ax', 'Ex'.
Do not include explanations, commentary, or extra text inside and outside the <proof>...</proof> tags.
 """
