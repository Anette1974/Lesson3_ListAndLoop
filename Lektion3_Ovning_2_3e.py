print("Övning 2, 3e - Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?")
movie_list = ["Änglagård", "Jönssonligan", "Mamma Mia", "Wallander"]
movie_list.append("Fellowship of the ring")
movie_list.insert(0,"The two towers")
print("\nFellowship of the ring är innan borttag av annan film på plats: ", movie_list.index("Fellowship of the ring"))
print("Listan innehåller nu filmerna:", movie_list)
#movie_list.remove("Jönssonligan")
movie_list.pop(1)
print("\nFellowship of the ring är efter borttag av annan film på plats: ", movie_list.index("Fellowship of the ring"))
print("Listan innehåller nu filmerna:", movie_list)