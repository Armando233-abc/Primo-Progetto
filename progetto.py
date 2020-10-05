import threading
import random, time


def voit_film():
    for i in range(250000):
        lista_film[random.choice(chiavi)] += 1

vincitore = ""

lista_film = {
"Oceania":0,
"Avatar":0,
"Il libro della giungla":0
}

chiavi = []

inizio = time.time()

for n in lista_film:
    chiavi.append(n)

th1 = threading.Thread(target=voit_film)
th2 = threading.Thread(target=voit_film)
th3 = threading.Thread(target=voit_film)
th4 = threading.Thread(target=voit_film)


th1.start()
th2.start()
th3.start()
th4.start()


th1.join()
th2.join()
th3.join()
th4.join()

for i in range(len(chiavi)):
    print(chiavi[i], ": ", lista_film[chiavi[i]], "voti")
    if(i == 0):
        vincitore = chiavi[i]
    if(lista_film[chiavi[i]] > lista_film[vincitore]):
        vincitore = chiavi[i]

fine = time.time()

print("\n\nil vincitore e' <<<<< ", vincitore, " >>>>> con ", lista_film[vincitore], " voti")
print("tempo: ", fine-inizio)