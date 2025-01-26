print("Övning 2, 3g - Vänd listan baklänges.")
movie_list = ["Änglagård", "Jönssonligan", "Mamma Mia", "Wallander"]
movie_list.append("Fellowship of the ring")
movie_list.insert(0,"The two towers")
print("\nListan innehåller nu filmerna:", movie_list)
#print(movie_list.reverse()) # FEL Ger endast värdet None tillbaks
movie_list.reverse()
print("\nListan baklänges ger filmerna: ", movie_list)