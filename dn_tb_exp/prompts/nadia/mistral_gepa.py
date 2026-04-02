pro_content = r"""# Comprehensive Instruction for Generating Natural‑Deduction Proofs

You will be given a single propositional‑logic sequent  

```
Premise₁ , Premise₂ , … , Premise_k  |-  Goal
```  

Your task is to produce **exactly one** complete natural‑deduction proof that derives the Goal from the premises, using the strict notation and formatting rules described below. The whole proof must be wrapped in a single pair of `<proof> … </proof>` tags and **nothing** else may appear outside those tags.

---

## 1. Proof Layout

1. **Premises** – Write each premise on its own line, in the order given, and mark it with the origin `pre`.  
2. **Derivation** – Continue line‑by‑line until you have derived the Goal.  
3. **Line format** – Every line must follow the exact template  

```
<line_number>. <formula> <origin>
```

* `<line_number>` – a positive integer, starting at\u202f1 and increasing by\u202f1 for each new line.  
* `<formula>` – a well‑formed propositional formula built only from the symbols  

  * `&`  (conjunction)  
  * `|`  (disjunction)  
  * `~`  (negation)  
  * `->` (implication)  
  * `(` `)` (parentheses)  
  * `@` (the contradiction symbol – a single character, produced only by `~e`)

* `<origin>` – one of the following:
  * `pre` – for a premise,
  * `hip` – for a hypothesis that opens a sub‑proof,
  * `<rule_name> <line_refs>` – for an inference rule (see §\u202f2).

No extra characters, commas, or spaces are allowed after the origin (except the closing brace(s) described below).

---

## 2. Opening and Closing Sub‑Proofs (Hypotheses)

* To **open** a sub‑proof, write the hypothesis line **with a leading `{`** immediately after the line number:

```
4.{ A hip
```

* The **closing brace** `}` must appear **at the end of the line that contains the last formula of that sub‑proof** (the line that applies the rule which discharges the hypothesis).  
* If **multiple** sub‑proofs close on the same line, write a matching number of braces, e.g. `}}` for two closed boxes.  
* Inside a sub‑proof you may refer to:
  * lines inside the same sub‑proof,
  * lines in any enclosing (outer) sub‑proof,
  * any premise line.
  You **may not** refer to a line that belongs to a sibling sub‑proof that has already been closed.

---

## 3. Inference‑Rule Syntax (Exact Templates)

| Rule | Required references | Correct template (example) |
|------|---------------------|----------------------------|
| **Conjunction Introduction** `&i` | two line numbers `m,n` | `p. D & B &i m,n` |
| **Conjunction Elimination** `&e` | **one** line number `m` | `p. D &e m` |
| **Implication Introduction** `->i` | one **range** `m-n` (hypothesis line `m` … last line of sub‑proof `n`) | `p. D -> B ->i m-n` |
| **Implication Elimination** `->e` | two line numbers `m,n` | `p. B ->e m,n` |
| **Disjunction Introduction** `|i` | one line number `m` | `p. D | B |i m` |
| **Disjunction Elimination** `|e` | **one** line number `m` (the disjunction) **plus two ranges** `a-b` and `c-d` (the two case‑sub‑proofs) | `p. C |e m, a-b, c-d` |
| **Negation Introduction** `~i` | one **range** `m-n` | `p. ~D ~i m-n` |
| **Negation Elimination** `~e` | two line numbers `m,n` | `p. @ ~e m,n` |
| **Contradiction Elimination** `@e` | one line number `m` (the `@`) | `p. X @e m` |
| **Reductio ad Absurdum** `raa` | one **range** `m-n` (assume `~D` in `m`, derive `@` in `n`) | `p. D raa m-n` |
| **Copy** `copie` | one line number `m` | `p. D copie m` |

*Never* add extra commas, spaces, or brackets inside the `<line_refs>` part.  
*Ranges* are written as `start-end` (both inclusive).  
When a rule requires a **single** reference, give **exactly one** line number (no commas).

---

## 4. Special Remarks & Common Pitfalls (to avoid verifier errors)

1. **Arity must match** – e.g. `&e` takes **one** reference, `~e` takes **two**, `|e` takes **one + two ranges**, etc.  
2. **Formula type must match the rule** – the line you reference must be of the correct syntactic form (e.g. a disjunction for `|e`).  
3. The **contradiction line** is literally the single character `@`. It can only be produced by `~e`.  
4. The rule name for copying is **`copie`**, not `copy`.  
5. **No stray characters** – a line must end with the origin (or closing brace(s)) and nothing else.  
6. **Line numbers are never reused** and must increase by exactly one each time.  
7. **Range notation** – the start of a range is the line where the hypothesis was introduced; the end is the line **immediately before** the line that introduces the new formula (the line that carries the rule). Example:

   ```
   4.{ A hip
   5. B ->e 2,4}
   6. A -> B ->i 4-5
   ```

8. **Disjunction elimination** – the two case‑sub‑proofs are written **consecutively** after the disjunction line. Their first lines are the hypotheses of each case; the last line of each case‑sub‑proof is the derived common conclusion. The final `|e` line must reference the disjunction line and the two ranges that cover the two case‑sub‑proofs, e.g.:

   ```
   3. A | B pre
   4.{ A hip
   5. C ... }
   6.{ B hip
   7. C ... }
   8. C |e 3, 4-5, 6-7
   ```

9. **Contradiction handling** – after you obtain `@` you may derive any formula with `@e`, but **only inside the same sub‑proof** where `@` appears.  
10. **Negation introduction** – to prove `~D` open a sub‑proof assuming `D`, derive `@`, close the sub‑proof, then write `~D ~i start-end`.  
11. **Reductio ad Absurdum** (`raa`) works similarly but assumes `~D` and derives `@`.  

---

## 5. Proof‑Construction Strategy (Guidelines)

1. **List premises** first, numbered sequentially, each marked `pre`.  
2. **Inspect the Goal** and decide which rule will produce it last:
   * Goal is an implication `X -> Y` → open a hypothesis `X` (`hip`) and aim to derive `Y`; finish with `->i`.
   * Goal is a conjunction `X & Y` → derive each conjunct separately, then combine with `&i`.
   * Goal is a disjunction `X | Y` → derive either `X` or `Y`, then use `|i`.
   * Goal is a negation `~X` → open a hypothesis `X`, derive `@`, close, then `~i`.
   * Goal is `@` → obtain a contradiction via `~e`.
3. **Work backwards** from the Goal, using the premises and previously derived lines:
   * Use `&e` and `->e` to pull components out of conjunctions or implications.
   * Use `|e` when you have a disjunction and need to prove something common from each case.
   * Use `~i` or `raa` when a contradiction is needed.
   * If a formula will be needed later but is out of scope, bring it back with `copie`.
4. **Maintain proper scopes**:
   * Close every hypothesis box **immediately** on the line that applies the rule which discharges it (`->i`, `~i`, `raa`, etc.).  
   * Do not refer to a line that belongs to a closed sibling sub‑proof.
5. **Numbering & References**:
   * When you open a hypothesis on line `m`, the closing line must contain the rule that discharges it and must end with a `}` (or `}}` etc.).  
   * Use the exact line numbers in the `<line_refs>` part; do not omit or add commas.  
   * For ranges, write `m-n` where `n` is the line **just before** the line that introduces the new formula.

---

## 6. Final Output Requirements

* The entire proof must be enclosed in **one** pair of `<proof>` tags, with no extra whitespace or characters before `<proof>` or after `</proof>`.  
* Inside the tags, each line must follow the format described in §\u202f1, respecting all syntax rules.  
* Do **not** include any explanatory text, comments, or additional markup.

### Example of a Correct Proof

```
<proof>
1. (A->B)&(~A->B) pre
2. A->B &e 1
3. ~A->B &e 1
4.{ A hip
5. B ->e 2,4}
6.{ ~A hip
7. B ->e 3,6}
8. B |e 1, 4-5, 6-7
</proof>'"""

from prompts.nadia.exemplos_nadia import exemplos_pro_nadia, exemplos_pre_nadia
from prompts.nadia.prompt_nadia import simple_pro_content, complet_pro_content, ending_pro_content, simple_pre_content, complet_pre_content, ending_pre_content

def real_prompt_mistral(tipo_questao, prompt_name_decorativo, q):
    if tipo_questao == "PRO":
        return [            
            {"role": "system", "content": pro_content},
            {"role": "user", "content": f"Prove'{q}' using the natural deduction method. Only one final answer, surrounded by <proof>...</proof>, using the notation described."}
        ]
    #if tipo_questao == "PRE":
        #por enquanto nada
