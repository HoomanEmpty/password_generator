def input_handler(name = "Value", low = -9.9e100, high = 9.9e100, Type = "str", options = []):
    data_type = {
        "str" : str,
        "float" : float,
        "int" : int,
        "bool" : bool}

    while True:
        try:
            if Type == "str":
                x = input(f"{name}: ").lower()
                if x in options or not options:
                    return x

                else:
                    print("The answer was not expected !\t", "Expected answer: ", [options[i] for i in range(len(options))])
            else:
                x = data_type[Type](input(f"{name}: "))
                if low <= x <= high:
                    return x
                
                else:
                    print("Out of range ! \t", low, "to", high)

        except ValueError:
            print(" Invalid input ...")
