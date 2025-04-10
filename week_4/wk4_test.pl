%% KB
restaurant(bellaItalia).
restaurant(sushiZen).
restaurant(burgerBarn).

cuisine(bellaItalia, italian).
cuisine(sushiZen, japanese).
cuisine(burgerBarn, fast_food).

rating(bellaItalia, high).
rating(sushiZen, moderate).
rating(burgerBarn, low).

offers_outdoor(bellaItalia, true).
offers_outdoor(sushiZen, false).
offers_outdoor(burgerBarn, false).

popular(bellaItalia, true).
popular(sushiZen, true).
popular(burgerBarn, false).

%% Rules using symbolic reasoning

upscale(Restaurant) :-
    restaurant(Restaurant),
    rating(Restaurant, high),
    popular(Restaurant, true).

recommended(Restaurant) :-
    upscale(Restaurant),
    offers_outdoor(Restaurant, true).

%% Natural language interpreter

interpret_result(Restaurant, NL) :-
    recommended(Restaurant),
    format(atom(NL), '~w is recommended because it has a high rating, is popular among locals, and offers outdoor seating.', [Restaurant]).

interpret_result(Restaurant, NL) :-
    \+ recommended(Restaurant),
    format(atom(NL), '~w is not recommended based on our criteria.', [Restaurant]).
