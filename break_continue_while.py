



def run():

    numbers = 0


    while numbers < 10:
        numbers += 1
        print(numbers)

        if numbers == 5:
            continue

        if numbers == 7:
            break
        print("Eso es todo amigos")




if __name__ == "__main__":
    run()