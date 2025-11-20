animelist = []
while True:
    anime_name = input("Enter the title of an anime (type 'exit' to finish): ")

    if anime_name.lower() == "exit":
         print("you have exited the anime program")
         break
    else: 
        animelist.append(anime_name)   
        print(f"{anime_name} has been added to your list.")
    
print("anime List added:")
for title in animelist:
    print(f"{title}")