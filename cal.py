while True:
    all_of_them = ['0','1','2','3','4','5','6','7','8','9','+','-','/','*','(',')']
    input_user = input("INPUT: ")
    try:
        input_user = input_user.replace(" ","")
        for everything in input_user:
            if everything not in all_of_them:
                raise ValueError
    except:
        print("Error input")
    else:
        def calculate(everything):
            result = eval(everything)
            return result
        result = calculate(input_user)
        print(f"OUTPUT: {result}")
        break
