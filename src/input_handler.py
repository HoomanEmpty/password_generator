def input_handler(name = "Value", low = -9.9e100, high = 9.9e100, Type = "str"):
    data_type = {
        "str" : str,
        "float" : float,
        "int" : int,
        "bool" : bool}

    while True:
        try:
            if Type == "str":
                return input(f"{name}: ")

            else:
                x = data_type[Type](input(f"{name}: "))
                if low <= x <= high:
                    return x
                
                else:
                    print("Out of range ! \t", low, "to", high)

        except ValueError:
            print(" Invalid input ...")
