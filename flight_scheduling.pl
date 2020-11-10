airport(toronto, 50, 60).
airport(madrid, 75, 45).
airport(malaga, 50, 30).
airport(barcelona, 40, 30).
airport(valencia, 40, 20).
airport(london, 75, 80).
airport(paris, 50, 60).
airport(toulouse, 40, 30).

myflight(toronto, iberia, madrid, 800, 480).
myflight(toronto, united, madrid, 950, 540).
myflight(toronto, aircanada, madrid, 900, 480).
myflight(toronto, aircanada, london, 500, 360).
myflight(toronto, united, london, 650, 420).
myflight(madrid, iberia, malaga, 50, 60).
myflight(malaga, iberia, valencia, 80, 120).
myflight(madrid, iberia, valencia, 40, 50).
myflight(madrid, aircanada, barcelona, 100, 60).
myflight(madrid, iberia, barcelona, 120, 65).
myflight(barcelona, iberia, valencia, 110, 75).
myflight(barcelona, iberia, london, 220, 240).
myflight(paris, united, toulouse, 35, 120).

flight(S, A, D, P, T) :- myflight(S, A, D, P, T) ; myflight(D, A, S, P, T).

% checks if a flight exists from city A to city B
isflight(S, D) :- (myflight(S, _, D, _, _) ; myflight(D, _, S, _, _) ). 

% checks if a flight from city A to city B with airline C is cheap
ischeap(S, D, A) :- ( ( myflight(S, A, D, P, _) ; myflight(D, A, S, P, _) ) , P < 400 ).

% checks if it is possible to travel from city A to city B with two flights
istwoflights(S, D) :- ( isflight(S, X) , isflight(X, D) ) -> write('It is possible. ') ; write('It is not possible').

% checks if a flight from city A to city B with airline C is preferred
ispreferred(S, D, A) :- ( ischeap(S, D, A) ; ( (myflight(S, A, D, _, _) ; myflight(D, A, S, _, _)) , A = aircanada ) ) -> write('The flight is preferred. ') ; write('Flight is not preferred. ').

% checks that there is a flight from city A to city B with Air Canada if there is a flight from A to B with United
flight_aircanada(S, D) :- myflight(S, united, D, _, _) ; myflight(D, united, S, _, _).
