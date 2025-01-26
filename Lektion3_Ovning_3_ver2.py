print("Övning 3, version 2 - Kvittouträknaren, loopa tills användaren skriver quit och summera sedan beloppen och dela upp på antalet gäster.")

sum_numbers = 0 #Summan av alla belopp
user_input = "" # Ber användaren om ett heltal eller quit
input_numbers = 0 # heltal från användaren, konverterat till integer
input_quests = 0
pay_quest = 0

print("\nVälkommen till Kvittokompis! Avsluta genom att skriva: quit")
while user_input != "quit": #kontrollera om användaren skrivit quit
    user_input = input("\nSkriv in ett belopp (heltal): ")  # Ber användaren skriva in ett belopp i heltal
    if user_input != "quit":
        input_numbers = int(user_input) # Konverterat inmatat belopp från sträng till heltal
        sum_numbers = sum_numbers + input_numbers #summerat redan inmatade tal med sum_numbers
    else:
        input_quests = int(input("Hur många gäster är ni? "))
        pay_quest = sum_numbers/input_quests
        print(f"Det blir {sum_numbers} kr totalt, alltså {pay_quest} kr per person. Välkommen åter!")