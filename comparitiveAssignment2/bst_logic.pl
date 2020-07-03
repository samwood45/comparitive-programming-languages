insert1(N, nil, tree(nil, N, nil)).
insert1(N, tree(L, B, T), tree(P, X, Y)) :- 
       (  N > B ->  insert1(N, T, Z), (P, X, Y) = (L, B, Z) ; (P, X, Y) = (L, B, T) 
	;N < B ->  insert1(N, L, Z), (P, X, Y) = (Z, B, T)).

insert([A|B], T0, T) :- insert1(A, T0, T1), insert(B, T1, T).
insert([], T, T).


search(N,tree(_,V,_)):- N =:= V.
search(N,tree(_,V,R)) :- N > V, search(V,R).
search(N,tree(L,V,_)) :- N < V, search(V,L).

