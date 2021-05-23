import random
import math

start = 2
end = 11

#Huomioita: tuottaa 132x = 330 (18), jossa m=6, mutta lopulta palautuu muotoon m=3. Lähtöarvot: a=4, b=10, m=6, c=11, k=3.

def congruentEq():
    """
    Ohjelma tuottaa muotoa ax=b (m) olevia kongruenssiyhtälöitä, joiden ratkaisemisessa
    pitää käyttää lausetta
        1) Olkoot kokonaisluvut a, b, m ja positiivinen kokonaisluku c.
                    ac=bc (mc) <-> a=b (m)
        eli saa 'supistaa' kaikista luvuista.  
        2) Olkoot kokonaisluvut a, b, c, m ja syt(c,m) = 1.
                    ac = bc (m) -> a = b (m)
    
    Lisäksi sievennetyin lopputulos on sellainen, että
            ax = b (m),
    missä a != 0.
    """
    
    a = random.randint(start, end)
    b = random.randint(start, end)
        
    m = random.randint(start + 3, end + 3)
    
    c = random.randint(start, end)
    k = random.randrange(start+1, end, 2)
    
    while(math.gcd(c,m) != 1):
        c = random.randint(start, end)
        m = random.randint(start + 3, end + 3)
    
    lauseke1 = a * c * k
    
    while(lauseke1 < 100 or lauseke1 > 500 or math.gcd(a,m) != 1 or a == b):
        a = random.randint(start, end)
        k = random.randrange(start+1, end, 2)
        lauseke1 = a * c * k
    
    lauseke2 = b * c * k
    modulo = m * k


    
    print("a={}, b={}, m={}, c={}, k={}".format(a, b, m, c, k))
    print("{}*{}*{}x = {}*{}*{} ({}*{})".format(a, c, k, b, c, k, m, k))
    print("{}x = {} ({})".format(lauseke1, lauseke2, modulo))
    
congruentEq()
