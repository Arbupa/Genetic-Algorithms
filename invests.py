import random


# function to show the table from our main content
def show_table() -> None:

    matrix = [[["Instrumento", "Rendimiento", "Monto inversion"]],
              [[1,                   "                10%             ",
                  1500]],
              [[2,                   "                11%             ",
                  5000]],
              [[3,                   "                13%             ",
                  10000]],
              [[4,                   "                10%             ",
                  8000]],
              [[5,                   "                9.5%            ",
                  6000]],
              [[6,                   "                10%             ",
                  5000]],
              ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j])
    print("\n")


# function to print each generation and their best invest row
def show_generation(generation: list) -> None:
    max_value = 0
    best_invest = []
    index = 0

    for i in range(len(generation)):
        if i > 0 and generation[i][6] < 30000:
            invest_val = generation[i][7]
            if max_value < invest_val:
                max_value = invest_val
                best_invest = generation[i]
                index = i

        print(generation[i])
    print(f"La mejor inversion es la numero: {index}\n", best_invest)


# function to calculate the inversion performance and
def calculate_inversion_performance(lista: list) -> list:
    inversion = [1500, 5000, 10000, 8000, 6000, 5000]
    rendimiento = [150, 550, 1300, 800, 570, 500]

    for i in range(len(lista)):
        # counter to know the index to add
        counter = 0
        inversion_sum = 0
        rendimiento_sum = 0

        for j in range(len(lista[i])):

            if lista[i][j] == 1 and counter < 6 and i > 0:
                inversion_sum = inversion_sum + inversion[counter]
                rendimiento_sum = rendimiento_sum + rendimiento[counter]

            if counter == 5 and i > 0:
                lista[i].append(inversion_sum)
                lista[i].append(rendimiento_sum)

            counter = counter + 1

    return lista


# function to create each generation based on the previous one
def create_generation(lista: list) -> list:
    # value to know if we should mutate or not
    mutate = random.randint(1, 100000)

    number_split = int(input("Ingresa número para hacer la partición: "))
    while number_split > 5 or number_split < 1:
        print("EL número no puede ser mayor a 5 o menor a 1")
        number_split = int(input("Ingresa número para hacer la partición: "))

    new_generation = []

    new_generation.append(lista[0])
    # create the generation's rows based on the previous list to
    # make their children
    new_row1 = lista[1][:number_split] + lista[2][number_split:6]
    new_row2 = lista[2][:number_split] + lista[1][number_split:6]
    new_row3 = lista[3][:number_split] + lista[4][number_split:6]
    new_row4 = lista[4][:number_split] + lista[3][number_split:6]
    new_row5 = lista[5][:number_split] + lista[6][number_split:6]
    new_row6 = lista[6][:number_split] + lista[5][number_split:6]

    new_generation.append(new_row1)
    new_generation.append(new_row2)
    new_generation.append(new_row3)
    new_generation.append(new_row4)
    new_generation.append(new_row5)
    new_generation.append(new_row6)

    # apply mutation to a random row and random number if the number is lower than 6
    if mutate < 6:
        first_randint = random.randint(1, 6)
        second_randint = random.randint(0, 5)

        val_to_mutate = new_generation[first_randint][second_randint]
        print("Fila antes de mutar: ",  new_generation[first_randint])

        if val_to_mutate == 0:
            new_generation[first_randint][second_randint] = 1
        else:
            new_generation[first_randint][second_randint] = 0

        print(
            f"Se mutó la fila numero: {first_randint} \ny se cambió el valor numero: {second_randint +1}")

    return new_generation


# function to create the first generation randomly
def create_first_generation() -> list:
    count = 0
    first_generation = [[1, 2, 3, 4, 5, 6, "Inversion", "Rendimiento"], ]
    inversion = [1500, 5000, 10000, 8000, 6000, 5000]
    rendimiento = [150, 550, 1300, 800, 570, 500]

    while count < 6:
        new_list = []
        inversion_suma = 0
        rendimiento_suma = 0

        for i in range(6):
            num = random.randint(0, 1)
            new_list.append(num)

            if num == 1:
                inversion_suma = inversion_suma + inversion[i]
                rendimiento_suma = rendimiento_suma + rendimiento[i]

        new_list.append(inversion_suma)
        new_list.append(rendimiento_suma)
        first_generation.append(new_list)

        count = count + 1

    return first_generation


# function to specify and create the number of generations
def number_of_generations() -> None:
    # list containing all the generations
    list_of_generations = []

    # while to handle if the user insert something different than a number and if is lower than 1
    while True:
        try:
            number = int(input("Ingresa numero de generaciones a crear: "))
            if number <= 1:
                print("¡Solo se pueden ingresar numeros mayores a 1!\n")
                continue
            break
        except:
            print("¡Solo se pueden ingresar numeros!\n")

    # create first generation, print it and add it to our list of generations
    lista_1 = create_first_generation()
    print("\n%%%%%%%%%% TABLA 1 %%%%%%%%%%%%")
    show_generation(lista_1)
    list_of_generations.append(lista_1)

    for i in range(number - 1):
        print(f"\n%%%%%%%%%% TABLA {i + 2} %%%%%%%%%%%%")
        lista_n = create_generation(list_of_generations[i])
        final_list = calculate_inversion_performance(lista_n)
        show_generation(final_list)
        list_of_generations.append(final_list)


if __name__ == "__main__":
    number_of_generations()
