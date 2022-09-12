#s = float(input('Informe o Seno: '))
#c = float(input('Informe o Coseno: '))
#t = float(input('Informe a Tangente: '))
#print('O Seno é igual a {}, o Coseno é {}, e a Tangente é {}'.format(s, c, t))

import math
an = float(input('Informe o Angulo desejado: '))
seno = math.sin(math.radians(an))
print('O Angulo de {:.2f} tem o SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O Angulo de {:.2f} tem o COSSENO de {:.2f}'.format(an, cosseno))
tan = math.tan(math.radians(an))
print('O angulo de {:.2f} tem a TANGENTE de {:.2f}'.format(an, tan))
#FORMA SIMPLIFICADA
from math import radians, sin, cos, tan
an = float(input('Informe o Angulo desejado: '))
seno = sin(math.radians(an))
print('O Angulo de {:.2f} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(math.radians(an))
print('O Angulo de {:.2f} tem o COSSENO de {:.2f}'.format(an, cosseno))
tan = tan(math.radians(an))
print('O angulo de {:.2f} tem a TANGENTE de {:.2f}'.format(an, tan))
