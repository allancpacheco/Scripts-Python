# Montando piramide no Python

import speedtest

test = speedtest.Speedtest()

down = test.download()
rsDonw = round(down)
fDown = int(rsDonw / 1e+6)

upload = test.upload()
rsUp = round(upload)
fUp = int(rsUp / 1e+6)

print (f'Sua velocidade de dowload e de {fDown} mb/s')
print (f'Sua velocidade de upload e de {fUp} mb/s')