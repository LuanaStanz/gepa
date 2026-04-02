pro_content = r"""# Instruction Set for Generating Natural‑Deduction Proofs


You will be given a **single propositional‑logic sequent** of the form  

```Premise₁ , Premise₂ , … , Premise_k  |-  Conclusion
```

Your task is to output **exactly one** well‑formed natural‑deduction proof that derives the
Conclusion from the listed premises.  
The whole proof must be enclosed between a single pair of tags:

``
<proof>
…proof lines…
</proof>
```

No other text, comments, or blank lines may appear outside these tags.
Below are **complete, unambiguous rules** for the language, layout, allowed symbols,
inference rules, and common pitfalls. Follow them *exactly*; otherwise the verifier will reject the answer.
---
## 1. Allowed Characters
Only the following characters may appear **anywhere** (including inside formulas,
line numbers, justifications, and braces):

```
& | ~ -> @ ( ) { }
```

Do **not** use any other symbols (e.g. “∧”, “∨”, “¬”, “→”, “⊢”, “∴”, commas, semicolons,
colons, periods other than the one after the line number, etc.).

---
## 2. Overall Proof Layout

| Element | Required format |
|---------|-----------------|
| **Premise line** | `<n>. <formula> pre` |
| **Copy line**    | `<n>. <formula> copie  <m>` (copy formula from line *m*) |
| **Inference line** | `<n>. <formula> <rule>  <references>` |
| **Hypothesis (subproof) start** | `<m.{ <H> hip` (no space before the `{`) |
| **Line inside a subproof** | Same format as ordinary lines (premise, copy, inference). |
| **Subproof closing** | The **last** line inside the box must end with a right brace `}` **immediately after** the justification (and after any references). No space before the brace. |
| **Discharging line** (→i, ~i, raa) | Appears **immediately** after the line that closed the subproof. Format: `<p>. <conclusion> <rule>  <m‑n>` where *m* is the line that opened the box and *n* is the line that closed it. |
| **Final line** | Must be the Conclusion formula; its justification may be any rule (including `copie`). |

### Line‑numbering

* Numbers start at **1** and increase by **1** for every new line (including hypothesis‑starter lines).
* The line number is followed directly by a period (`.`) and **one** space.
* After the space comes the formula, then **one** space, then the justification keyword, then (if required) **one** space and the reference list.

### Reference list syntax

* A reference is either a single line number (`3`) or an inclusive range (`2-5`).
* When a rule needs several references they must be separated by **commas with no spaces** (e.g. `->e 2,5`).
* For `|e` the three references must be written exactly as  

  ```
  |e  m, (m+1)-n, (n+1)-p
  ```

  where *m* is the line of the disjunction, *(m+1)-n* is the first subproof range, and *(n+1)-p* is the second subproof range.

---

## 3. Inference Rules (exact keywords and required patterns)

| Rule | Required pattern (what must already exist) | How to write the line |
|------|--------------------------------------------|-----------------------|
| **Conjunction Introduction** `&i` | lines `a. A` and `b. B` (both currently in scope) | `<c>. A & B &i  a,b` |
| **Conjunction Elimination** `&e` | line `a. A & B` | `<c>. A &e  a` **or** `<c>. B &e  a` |
| **Implication Introduction** `->i` | a **closed** subproof `m.{ A hip … n. B }` (B is the last line **inside** the box) | `<p>. A -> B ->i  m-n` (must be the line **immediately after** the closing brace) |
| **Implication Elimination** `->e` | lines `a. A -> B` and `b. A` | `<c>. B ->e  a,b` |
| **Disjunction Introduction** `|i` | line `a. A` (or `a. B`) | `<c>. A | B |i  a` **or** `<c>. B | A |i  a` |
| **Disjunction Elimination** `|e` | line `a. A | B` and two **closed** subproofs:  

  ```
  a+1.{ A hip … x. C }
  x+1.{ B hip … y. C }
  ``` | `<z>. C |e  a, (a+1)-x, (x+1)-y` (the line *z* is the first line **after** the second closing brace) |
| **Negation Introduction** `~i` | a **closed** subproof `m.{ B hip … n. @ }` (where `@` is a contradiction) | `<p>. ~B ~i  m-n` (immediately after the closing brace) |
| **Negation Elimination** `~e` | lines `a. A` and `b. ~A` | `<c>. @ ~e  a,b` |
| **Contradiction Elimination** `@e` | inside a subproof: line `a. @` and later line `b. C` (any formula) | `<b>. C @e  a` |
| **Reductio ad Absurdum** `raa` | a **closed** subproof `m.{ ~A hip … n. @ }` | `<p>. A raa  m-n` (immediately after the closing brace) |
| **Copy** `copie` | line `a. A` | `<b>. A copie  a` |

*All references must refer to lines that are **still in scope** at the moment the rule is applied.*  
If a line belongs to a subproof that has already been closed, you may only refer to it after you have **copied** it to an earlier line.

---

## 4. Scope & Subproof Discipline

1. **Opening a hypothesis** (`hip`) starts a new *box*. The box remains open until the line that ends with `}`.
2. **Closing a box**: the line that contains the `}` is still a normal inference line; the brace merely indicates that the box ends there.
3. **Discharging** (`->i`, `~i`, `raa`) **must be the very next line** after the line that closed the box. No other lines may intervene.
4. After a box is closed you may reference:
   * Premises,
   * Formulas derived **outside** the closed box,
   * Formulas that were **copied** from inside the box before it was closed.
5. **Never** reference a line that belongs to a closed box **unless** you have first created a copy of that line.
6. **Nested boxes** are allowed. When you close several nested boxes on the same line, write the closing braces consecutively (`}}` or `}}}`) after the justification.

---

## 5. Exact Syntax Checklist (must hold for **every** line)

1. `<num>.` – number followed directly by a period, no extra spaces.
2. One space after the period.
3. The formula, built only from the allowed symbols.
4. One space.
5. Justification keyword (`pre`, `hip`, `copie`, `&i`, `&e`, `->i`, `->e`, `|i`, `|e`, `~i`, `~e`, `@e`, `raa`).
6. If the rule needs references, put **one** space after the keyword, then the reference list exactly as described.
7. If the line **closes** a subproof, append a right brace `}` **immediately** after the justification (and after any references). No space before the brace.
8. No trailing spaces, no blank lines, no extra characters.

---

## 6. Proof‑Construction Strategies (quick guide)

Below are typical patterns you will need for most exercises. Use them verbatim; they guarantee a correct structure.

### 6.1 Proving an Implication `A -> B`
```
m.{ A hip
   … derive B …
n. B   … (any rule) … }
p. A -> B   ->i  m-n
```

### 6.2 Proving a Negation `~A`
```
m.{ A hip
   … derive a contradiction @ …
n. @   … (any rule) … }
p. ~A   ~i  m-n
```

### 6.3 Proving a Contradiction `@`
Obtain a formula `C` and its negation `~C` in the same scope, then:

```
p. @   ~e  line_of_C,line_of_~C
```

### 6.4 Reductio ad Absurdum (prove `A` by assuming `~A`)
```
m.{ ~A hip
   … derive @ …
n. @   … }
p. A   raa  m-n
```

### 6.5 Conjunction `A & B`
*To introduce*: have `A` and `B` in scope → `&i`.  
*To eliminate*: from `A & B` use `&e` to get either conjunct.

### 6.6 Disjunction `A | B`
*To introduce*: from `A` (or `B`) use `|i`.  
*To eliminate*: you need a proof of the desired conclusion `C` from `A` and another proof of the same `C` from `B`:

```
k. A | B   pre
k+1.{ A hip
      … derive C …
k+? . C   … }          // close first subproof
k+?+1.{ B hip
        … derive C …
k+?+? . C   … }        // close second subproof
k+?+?+1. C   |e  k, (k+1)-k1, (k+?+1)-k2
```

### 6.7 Using a Premise Inside a Subproof
Premises are always in scope, even inside subproofs. No need to copy them.

### 6.8 When a Formula Will Be Needed **After** a Subproof Is Closed
Copy it **before** the closing brace:

```
m.{ … 
   q. X   … }
r. X   copie  q   // now X is available outside the box
```

### 6.9 Common Error‑Avoidance Checklist
* The hypothesis line must be `m.{ H hip` (no extra text, no missing `{`).
* The line that closes a box must end with `}`; the brace is **not** a separate line.
* The discharge line (`->i`, `~i`, `raa`) must be **immediately** after the closing line; do not insert any other inference between them.
* All references in a rule must refer to lines that are still in scope **at that moment**.
* Do **not** reference a line that belongs to a closed box unless you have first copied it.
* When using `|e`, the three reference parts must be exactly `m, (m+1)-n, (n+1)-p` with commas, parentheses, and no spaces.
* Do not place any spaces before a closing brace `}`.
* Do not use any forbidden symbols (including commas inside formulas, semicolons, colons, etc.).

---

## 7. Full Example (correctly formatted)

Problem: `A->(B&C) |- (A->B)&(A->C)`

```
<proof>
1. A -> (B & C) pre
2.{ A hip
3. B & C   ->e 1,2
4. B       &e 3 }
5. A -> B   ->i 2-4
6.{ A hip
7. B & C   ->e 1,6
8. C       &e 7 }
9. A -> C   ->i 6-8
10. (A -> B) & (A -> C)   &i 5,9
</proof>'"""

from prompts.nadia.exemplos_nadia import exemplos_pro_nadia, exemplos_pre_nadia
from prompts.nadia.prompt_nadia import simple_pro_content, complet_pro_content, ending_pro_content, simple_pre_content, complet_pre_content, ending_pre_content
#todas regras: complet_pro_content+complet_pre_content

def real_prompt_phi4(tipo_questao, prompt_name_decorativo, q):
    if tipo_questao == "PRO":
        return [            
            {"role": "system", "content": pro_content},
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    #if tipo_questao == "PRE":
        #por enquanto nada
