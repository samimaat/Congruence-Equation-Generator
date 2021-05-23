import random
import math

start = 2
end = 11

#Huomioita: tuottaa 132x = 330 (18), jossa m=6, mutta lopulta palautuu muotoon m=3. Lähtöarvot: a=4, b=10, m=6, c=11, k=3.

def congruentEq():
    """
    The program generates congruence equations of form
        ax=b (m), 
    which you have to solve by utilizing the following conjectures
    
    1) Let a, b and m be integers and a positive integer c so that
        ac = bc (mc) <-> a = b (m).
    2) Let numbers a, b, c and m be integers and gcd(c,m) = 1 so that
        ac = bc (m) -> a = b (m).
    
    Simple form of the congruence equation is 
        ax = b (m),
    where a != 0.
    """
    
    a = random.randint(start, end)
    b = random.randint(start, end)
        
    m = random.randint(start + 3, end + 3)
    
    c = random.randint(start, end)
    k = random.randrange(start+1, end, 2)
    
    while(math.gcd(c,m) != 1):
        c = random.randint(start, end)
        m = random.randint(start + 3, end + 3)
    
    exp1 = a * c * k
    
    while(exp1 < 100 or exp1 > 500 or math.gcd(a,m) != 1 or a == b):
        a = random.randint(start, end)
        k = random.randrange(start+1, end, 2)
        exp1 = a * c * k
    
    exp2 = b * c * k
    modulo = m * k

    print("a={}, b={}, m={}, c={}, k={}".format(a, b, m, c, k))
    print("{}*{}*{}x = {}*{}*{} ({}*{})".format(a, c, k, b, c, k, m, k))
    print("{}x = {} ({})".format(exp1, exp2, modulo))
    
congruentEq()
