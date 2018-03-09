list_var = ["123456789", "45646546", "825662", "0323123"]
list_iter = iter(list_var)
for i in range(1, 5):
    string = next(list_iter)
    print(string)
