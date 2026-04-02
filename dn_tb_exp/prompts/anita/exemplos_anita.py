exemplos_pro_anita = [
    {"user": "Prove '(A | B) & (A | C) |- A | (B & C)', using the analytical tableau method. Final answer using the notation described. ",
    "assistant": r''' <proof>
                        1. T (A | B) & (A | C) pre
                        2. F A | (B & C) conclusion
                        3. T (A | B) 1 
                        4. T (A | C) 1 
                        5. F A 2      
                        6. F (B & C) 2  
                        7. {T A 3 
                        8.  @ 5,7} 
                        9. {T B 3 
                        10.  {T A 4 
                        11.   @ 5,10} 
                        12.  {T C 4
                        13.     {F B 6 
                        14.      @ 9,13}  
                        15.      {F C 6 
                        16.       @ 12,15}}} 
                    </proof>'''
    },
    {"user": "Prove '|- (~A -> B) -> ((~A -> ~B) -> A)', using the analytical tableau method. Final answer using the notation described.", 
     "assistant": r''' <proof>
                            1. F (~A -> B) -> ((~A -> ~B) -> A) conclusion
                            2. T (~A -> B) 1 
                            3. F ((~A -> ~B) -> A) 1 
                            4. T (~A -> ~B) 3 
                            5. F A 3 
                            6.  {F ~A 2 
                            7.   T A 6 
                            8.   @ 5,7}
                            9.  {T B 2 
                            10.   { F ~A 4 
                            11.     T A 10
                            12.     @ 5,11}
                            13.   {T ~B 4 
                            14.    F B 13 
                            15.    @ 9,14}}
                        </proof>'''
    },
    {"user": "Prove '~(~A | ~B) |- A & B', using the analytical tableau method. Final answer using the notation described.",
      "assistant": r'''<proof>
                            1. T ~(~A | ~B) pre 
                            2. F A & B conclusion 
                            3. F (~A | ~B) 1 
                            4. F ~A 3 
                            5. F ~B 3 
                            6. T A 4 
                            7. T B 5 
                            8. {F A 2 
                            9.  @ 6,8} 
                            10. {F B 2 
                            11. @ 7,10} 
                        </proof>'''
    },
    {"user": "Prove '~B -> ~A |- A -> B', using the analytical tableau method. Final answer using the notation described.", 
     "assistant": r'''<proof>
                        1. T ~B -> ~A pre
                        2. F A -> B conclusion
                        3. T A 2 
                        4. F B 2
                        5. {F ~B 1 
                        6. T B 5
                        7.  @ 6,4} 
                        8. {T ~A 1 
                        9. F A 8 
                        10. @ 9,3} 
                    </proof>'''
    },
    {"user": "Prove '~A | ~B |- ~(A & B)', using the analytical tableau method. Final answer using the notation described.", 
     "assistant": r'''<proof>
                        1. T ~A|~B pre
                        2. F ~(A & B) conclusion
                        3. T A & B 2 
                        4. T A  3
                        5. T B  3 
                        6. {T ~A 1 
                        7. F A 6
                        8. @ 7, 4} 
                        9. {T ~B 1 
                        10. F B 9 
                        11. @ 10,5}
                    </proof>'''
    }
] 

exemplos_pre_anita = [ #6[Ex P(x), Ax (P(x)->Q(x)) |- Ex Q(x)], 1[Ax (P(x)|P(x)) |- Ax P(x)], 4[|- Ex (D(x)&K(x))->(Ex D(x)|Ex K(x))]
    {"user": "Prove 'Ex P(x), Ax (P(x)->Q(x)) |- Ex Q(x)', using the analytical tableau method. Final answer using the notation described. ",
    "assistant": r''' <proof>
                        1. T Ex P(x) pre
                        2. T Ax (P(x)->Q(x)) pre
                        3. F Ex Q(x) conclusion
                        4. T P(a) 1 
                        5. T (P(a)->Q(a)) 2 
                        6. F Q(a) 3 
                        7.{ F P(a) 5 
                        8. @ 4,7}    
                        9.{ T Q(a) 5 
                        10. @ 6,9}   
                    </proof>'''
    },
    {"user": "Prove 'Ax (P(x)|P(x)) |- Ax P(x)', using the analytical tableau method. Final answer using the notation described.", 
     "assistant": r''' <proof>
                            1. T Ax (P(x)|P(x)) pre 
                            2. F Ax P(x) conclusion
                            3. F P(a) 2          
                            4. T (P(a)|P(a)) 1   
                            5.{ T P(a) 4         
                            6. @ 3,5}            
                            7.{ T P(a) 4         
                            8. @ 3,7}            
                        </proof>'''
    },
    {"user": "Prove '|- Ex (D(x)&K(x))->(Ex D(x)|Ex K(x))', using the analytical tableau method. Final answer using the notation described.",
      "assistant": r'''<proof>
                            1. F (Ex (D(x)&K(x)) -> (Ex D(x) | Ex K(x))) conclusion
                            2. T Ex (D(x)&K(x)) 1 
                            3. F (Ex D(x) | Ex K(x)) 1
                            4. T (D(a)&K(a)) 2 
                            5. T D(a) 4 
                            6. T K(a) 4 
                            7. F Ex D(x) 3 
                            8. F Ex K(x) 3 
                            9. F D(a) 7 
                            10. @ 5,9 
                        </proof>'''
    },
    {"user": "Prove 'Ax ~(P(x)&~Q(x)), Ax ~Q(x) |- Ax ~P(x)	', using the analytical tableau method. Final answer using the notation described.", 
     "assistant": r'''<proof>
                         1. T Ax ~(P(x)&~Q(x)) pre 
                        2. T Ax ~Q(x) pre 
                        3. F Ax ~P(x) conclusion 
                        4. F ~P(a) 3         
                        5. T P(a) 4           
                        6. T ~(P(a)&~Q(a)) 1  
                        7. T ~Q(a) 2          
                        8. F (P(a)&~Q(a)) 6   
                        9.{ F P(a) 8          
                        10. @ 5,9}           
                        11.{ F ~Q(a) 8        
                        12. @ 7,11}      
                    </proof>'''
    },
    {"user": "Prove '|- Ex P(x)->~Ax ~P(x)', using the analytical tableau method. Final answer using the notation described.", 
     "assistant": r'''<proof>
                        1. T Ex (P(x)&~Q(x)) pre 
                        2. F ~Ax (P(x)->Q(x)) conclusion 
                        3. T (P(a)&~Q(a)) 1 
                        4. T P(a) 3 
                        5. T ~Q(a) 3 
                        6. T Ax (P(x)->Q(x)) 2 
                        7. T (P(a)->Q(a)) 6 
                        8.{ F P(a) 7 
                        9. @ 4,8} 
                        10.{ T Q(a) 7 
                        11. F Q(a) 5  
                        12. @ 10,11}
                    </proof>'''
    }
] 
