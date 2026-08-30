def input_handler(name = "Value", low = -9.9e100, high = 9.9e100, Type = "str", options = [], default = "", automate = True):
    data_type = {
        "str" : str,
        "float" : float,
        "int" : int,
        "bool" : bool}

    while True:
        try:
            if Type == "str":
                x = input(f"{name}: ").lower() if automate else input(f"{name}: ")

                if x:
                    if x in options or not options:
                        return x

                    else:
                        print("\nThe answer was not expected !\t", "Expected answer: ", [options[i] for i in range(len(options))])

                else:

                    if automate:
                        return default.lower()

                    return default

            else:
                x = input(f"{name}: ")

                if x: 
                    x = data_type[Type](x)

                    if low <= x <= high:
                        return x
                    
                    else:
                        print("\nOut of range! Please enter a value between ", low, "and ", high, "\n") 

                else:
                    return default

        except ValueError:
            print(" Invalid input ...")
