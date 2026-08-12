def input_handler(name = "Value", low = -9.9e100, high = 9.9e100, Type = "str", options = [], default = ""):
    data_type = {
        "str" : str,
        "float" : float,
        "int" : int,
        "bool" : bool}

    while True:
        try:
            if Type == "str":
                x = input(f"{name}: ").lower()

                if x:
                    if x in options or not options:
                        return x

                    else:
                        print("The answer was not expected !\t", "Expected answer: ", [options[i] for i in range(len(options))])

                else:
                    return default.lower()

            else:
                x = input(f"{name}: ")

                if x: 
                    x = data_type[Type](x)

                    if low <= x <= high:
                        return x
                    
                    else:
                        print("Out of range ! \t", low, "to", high, "\n")

                else:
                    return default

        except ValueError:
            print(" Invalid input ...")
