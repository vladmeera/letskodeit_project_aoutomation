def function_dict(func_name: str, num_a: int, num_b: int):
    def add(a, b):
        print("adding")
        return a + b

    def subtract(a, b):
        print("subtracting")
        return a - b

    fuct_map = {"add": add, "subtract": subtract}
    return fuct_map[func_name](num_a, num_b)


result = function_dict("add", 2, 3)
print(result)
