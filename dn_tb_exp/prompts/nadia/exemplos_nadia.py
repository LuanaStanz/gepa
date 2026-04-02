exemplos_pro_nadia = [
    {"user": "Prove '(A->B)&(~A->B) |- B', using the natural deduction method. Final answer using the notation described. ",
    "assistant": r''' <proof>
                        1. (A -> B) & (~A -> B) pre
                        2. A -> B &e 1
                        3. ~A -> B &e 1
                        4. { ~(A | ~A) hip
                        5. { A hip
                        6. A | ~A |i 5
                        7. @ ~e 6,4}
                        8. ~A ~i 5-7
                        9. A | ~A |i 8
                        10. @ ~e 9,4}
                        11. A | ~A raa 4-10
                        12. { A hip
                        13. B ->e 12,2}
                        14. { ~A hip
                        15. B ->e 14,3}
                        16. B |e 11, 12-13, 14-15
                        </proof>'''
    },
    {"user": "Prove 'A|B |- (~A->B)&(~B->A)', using the natural deduction method. Final answer using the notation described.", 
     "assistant": r''' <proof>
                        1. A | B pre
                        2. {~A hip
                        3. {A hip
                        4. @ ~e 2,3
                        5. B @e 4}
                        6. {B hip
                        7. B copie 6}
                        8. B |e 1,3-5,6-7}
                        9. ~A -> B ->i 2-8
                        10. {~B hip
                        11. {A hip
                        12. A copie 11}
                        13. {B hip
                        14. @ ~e 10,13
                        15. A @e 14}
                        16. A |e 1,11-12,13-15}
                        17. ~B -> A ->i 10-16
                        18. (~A -> B) & (~B -> A) &i 9,17
                        </proof>'''
    },
    {"user": "Prove '~(A&B) |- ~A|~B', using the natural deduction method. Final answer using the notation described.",
      "assistant": r'''<proof>
                        1. ~(A & B) pre 
                        2. { ~(~A | ~B) hip 
                        3. { ~A hip 
                        4. ~A | ~B |i 3 
                        5. @ ~e 4, 2 } 
                        6. A raa 3-5 
                        7. { ~B hip 
                        8. ~A | ~B |i 7 
                        9. @ ~e 8, 2 } 
                        10. B raa 7-9 
                        11. A & B &i 6, 10 
                        12. @ ~e 11, 1 } 
                        13. ~A | ~B raa 2-12 
                        </proof>'''
    },
    {"user": "Prove '~S->~R, (P&Q)|R, ~S->~Q |- ~P|S', using the natural deduction method. Final answer using the notation described.", 
     "assistant": r'''<proof>
                        1. (~S->~R)				pre
                        2. ((P&Q)|R)				pre
                        3. (~S->~Q)				pre
                        4. { (P&Q)				hip
                        5.   Q					&e 4
                        6.   { ~S				hip
                        7.     ~Q				->e 6,3
                        8.     @				~e 5,7}
                        9.   S					raa 6-8}
                        10. { R					hip
                        11.   { ~S				hip
                        12.      ~R				->e 1,11
                        13.      @				~e 10,12}
                        14.   S					raa 11-13}
                        15. S					|e 2,4-9,10-14
                        16. (~P|S)				|i 15
                        </proof>'''
    },
    {"user": "Prove '~(A->~B) |- A&B', using the natural deduction method. Final answer using the notation described.", 
     "assistant": r'''<proof>
                        1. ~ (A -> ~ B) pre 
                        2. { ~ A hip 
                        3. { A hip 
                        4. @ ~e 2,3 
                        5. ~B @e 4 } 
                        6. A->~B ->i 3-5 
                        7. @ ~e 6,1 } 
                        8. A raa 2-7 
                        9. { ~ B hip 
                        10. { A hip 
                        11. ~ B copie 9 } 
                        12. (A -> ~ B) ->i 10-11 
                        13. @ ~e 12, 1 } 
                        14. B raa 9-13 
                        15. A & B &i 8, 14 
                        </proof>'''
    },
] 

exemplos_pre_nadia = [
    {"user": "Prove '|- (P->Ex Q(x))->Ex (P->Q(x))', using the natural deduction method. Final answer using the notation described. ",
    "assistant": r''' <proof>
                        1. { 	(P -> Ex Q(x))					hip
                        2.	{	~(~P | Ex Q(x))					hip
                        3.		{	P								      hip
                        4.      Ex Q(x)               ->e 3, 1
                        5.			~P | Ex Q(x)					|i 4
                        6.			@								~e 5,2 }		
                        7.		~P									~i 3-6
                        8.		~P | Ex Q(x)						|i 7
                        9.		@									~e 8,2 }
                        10.	~P | Ex Q(x)        raa 2-9
                        11.	{	~P									hip
                        12.		{	P								hip
                        13.			@								~e 11,12
                        14.     Q(a)            @e 13 }
                        15.		P -> Q(a)							->i 12-14
                        16.		Ex  (P -> Q(x))					Ei 15 }
                        17.	{	Ex Q(x)							hip
                        18.		{ a		Q(a)						hip
                        19.			{	P							hip
                        20.				Q(a)						copie 18 }
                        21.			P -> Q(a)						->i 19-20
                        22.			Ex (P -> Q(x))				Ei 21 }
                        23.		Ex (P -> Q(x))					Ee 17, 18-22 }
                        24.	Ex (P -> Q(x))						|e 10, 11-16, 17-23}
                        25. (P -> Ex Q(x)) -> Ex (P -> Q(x))	->i 1-24
                    </proof>'''
    },
    {"user": "Prove 'Ax ((P(x)->Q(x))&(Q(x)->P(x))) |- Ax ((~P(x)->~Q(x))&(~Q(x)->~P(x)))', using the natural deduction method. Final answer using the notation described.", 
     "assistant": r''' <proof>
                            1. Ax((P(x) -> Q(x)) & (Q(x) -> P(x))) pre
                            2. { a
                            3.   (P(a) -> Q(a)) & (Q(a) -> P(a)) Ae 1
                            4.   P(a) -> Q(a) &e 3
                            5.   Q(a) -> P(a) &e 3
                            6.   { ~Q(a) hip
                            7.     { P(a) hip
                            8.       Q(a) ->e 7,4
                            9.       @ ~e 6,8 }
                            10.   ~P(a) ~i 7-9 }
                            11. ~Q(a) -> ~P(a) ->i 6-10
                            12. { ~P(a) hip
                            13.   { Q(a) hip
                            14.     P(a) ->e 13,5
                            15.     @ ~e 12,14 }
                            16.   ~Q(a) ~i 13-15 }
                            17. ~P(a) -> ~Q(a) ->i 12-16
                            18. (~P(a) -> ~Q(a)) & (~Q(a) -> ~P(a)) &i 17,11 }
                            19. Ax((~P(x) -> ~Q(x)) & (~Q(x) -> ~P(x))) Ai 2-18 
                        </proof>'''
    },
    {"user": "Prove 'Ax Ey (P(x)|Q(y)) |- Ey Ax (P(x)|Q(y))', using the natural deduction method. Final answer using the notation described.",
      "assistant": r'''<proof>
                            1. AxEy(P(x)|Q(y))					pre
                            2. { 	~EyAx(P(x)|Q(y))				hip
                            3.	{ a
                            4.		{	Ax(P(x)|Q(a))			hip
                            5.			EyAx(P(x)|Q(y))			Ei 4
                            6.			@				~e 2,5 }
                            7.		~Ax(P(x)|Q(a))				~i 4-6 }
                            8.	Ay~Ax(P(x)|Q(y))				Ai 3-7
                            9.	{ a
                            10.		~Ax(P(x)|Q(a))				Ae 8
                            11.		{	~Ex~(P(x)|Q(a))			hip
                            12.			{ b
                            13.				{ 	~(P(b)|Q(a))	hip
                            14.					Ex~(P(x)|Q(a))	Ei 13
                            15.					@		~e 11,14 }
                            16.				P(b)|Q(a)		raa 13-15 }
                            17.			Ax(P(x)|Q(a))			Ai 12-16
                            18.			@				~e 10,17 }
                            19.		Ex~(P(x)|Q(a))				raa 11-18 }	
                            20.	AyEx~(P(x)|Q(y))				Ai 9-19
                            21.    	Ex ~(P(x)|Q(b))					Ae 20
                            22.	{ a	~(P(a)|Q(b))				hip
                            23.		Ey(P(a)|Q(y))				Ae 1		
                            24.		{ c	P(a)|Q(c)			hip
                            25.			{	P(a)			hip
                            26.				P(a)|Q(b)		|i 25
                            27.				@			~e 22,26 }
                            28.			{	Q(c)			hip
                            29.				Ex ~(P(x)|Q(c))		Ae 20
                            30.				{ d	~(P(d)|Q(c))	hip
                            31.					P(d)|Q(c)	|i 28
                            32.					@		~e 30,31 }
                            33.				@			Ee 29, 30-32 }
                            34.			@				|e 24, 25-27, 28-33 }
                            35.		@					Ee 23, 24-34  }	
                            36.	@						Ee 21, 22-35 }
                            37. EyAx(P(x)|Q(y))					raa 2-36
                        </proof>'''
    },
    {"user": "Prove '|- Ax (P(x)|Q)->(Ax P(x)|Q)', using the natural deduction method. Final answer using the notation described.", 
     "assistant": r'''<proof>
                        1. { Ax(P(x) | Q) hip 
                        2. { ~(Ax P(x) | Q) hip 
                        3. { a 
                        4. P(a) | Q Ae 1 
                        5. { P(a) hip } 
                        6. { Q hip 
                        7. Ax P(x) | Q |i 6 
                        8. @ ~e 7,2 
                        9. P(a) @e 8 } 
                        10. P(a) |e 4, 5-5, 6-9 } 
                        11. Ax P(x) Ai 3-10 
                        12. Ax P(x) | Q |i 11 
                        13. @ ~e 2,12 } 
                        14. Ax P(x) | Q raa 2-13 } 
                        15. Ax(P(x) | Q) -> (Ax P(x) | Q) ->i 1-14
                    </proof>'''
    },
    {"user": "Prove 'Ax (~H(x)|M(x)), Ex H(x) |- Ex M(x)', using the natural deduction method. Final answer using the notation described.", 
     "assistant": r'''<proof>
                        1. Ax (~H(x)|M(x)) pre 
                        2. Ex H(x) pre 
                        3. { a H(a) hip 
                        4. ~H(a)|M(a) Ae 1 
                        5. { ~H(a) hip 
                        6. @ ~e 3,5 
                        7. Ex M(x) @e 6 } 
                        8. { M(a) hip 
                        9. Ex M(x) Ei 8 } 
                        10. Ex M(x) |e 4, 5-7, 8-9 } 
                        11.Ex M(x) Ee 2, 3-10
                    </proof>'''
    },
] 