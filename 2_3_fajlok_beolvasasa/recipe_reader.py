def recipe_reader(file_name):
    file = open(file_name)
    ingradients = []

    for line in range(0,8):
        ingradients.append(file.readline())
    
    file.close()

    print(ingradients)

recipe_reader('2_3_fajlok_beolvasasa/recipe.txt')