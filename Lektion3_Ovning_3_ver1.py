print("Övning 3, version 1 - Kvittouträknaren, loopa tills användaren skriver quit och summera sedan beloppen.")

sum_numbers = 0 #Summan av alla belopp
user_input = "" # Ber användaren om ett heltal eller quit
input_numbers = 0 # heltal från användaren, konverterat till integer

print("\nVälkommen till Kvittokompis! Avsluta genom att skriva: quit")
while user_input != "quit": #kontrollera om användaren skrivit quit
    user_input = input("\nSkriv in ett belopp (heltal): ")  # Ber användaren skriva in ett belopp i heltal
    if user_input != "quit":
        input_numbers = int(user_input) # Konverterat inmatat belopp från sträng till heltal
        sum_numbers = sum_numbers + input_numbers #summerat redan inmatade tal med sum_numbers
    else:
        print(f"Det blir {sum_numbers} kr totalt. Välkommen åter!")