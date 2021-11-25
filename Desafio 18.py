import math 

ang = float(input('Digite o angulo que voce deseja '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print ('Para o angulo de {:.2f} o seno e de {:.2f}, o cosseno e de {:.2f} e a tangente e de {:.2f}'.format(ang,sen,cos,tan))