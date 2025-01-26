#https://github.com/Anette1974/Lesson3_ListAndLoop.git
print("Övning 1, Diskutera i grupp")
print ("del 1, Vad skrivs ut?")
limit = 15
index = 5
while index <= limit:
    print(index)
    index = index + 2

print ("\ndel 2, Vad skrivs ut?") # Svar, siffrorna 1-4 och 6-9
for i in range(10):
    if i ==5:
        print(" ")
    else:
        print(i)
    i = i + 1

print ("\ndel 3, Vad blir summan?") # Svar, 6 (fel, rätt svar hade varit 15)
counter = 0
for i in range (6):
    counter += i
    print ("I loopen", counter)
print (counter)

print ("\ndel 4, Vad skrivs ut?")
x = 0
y = 1
while y < 10:
    if y % 2 ==0:
        x -= y #Tips, sätt brytpunkt här
    else:
        x += y*y # tips, sätt brytpunkt här
    y += 1

print("\ndel 5, Skriv ut 'time istället")
message = ("its_time_to_get_coding")
print (message[4:8])

print("\ndel 6, Vad skrivs ut? Kan du flytta linjen ett steg åt höger?")
for y in range(1,7):
    s = ""
    for x in range (1,9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)