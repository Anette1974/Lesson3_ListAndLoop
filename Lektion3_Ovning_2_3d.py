print("Övning 2, 3d - Ta reda på vilken position (index) 'Fellowship of the ring' har nu.")
movie_list = ["Änglagård", "Jönssonligan", "Mamma Mia", "Wallander"]
movie_list.append("Fellowship of the ring")
movie_list.insert(0,"The two towers")
print("Fellowship of the ring är på plats: ", movie_list.index("Fellowship of the ring"))