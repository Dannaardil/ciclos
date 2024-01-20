for multi in range(1,11):
    for multi2 in range(1,11):
        product = str(multi * multi2)
        if multi2 == 10 :
            output = product.rjust(3)
        else: 
            output = product.rjust(2)
        print(output,end = " ")
    print()

       