immutable_var = 3, 7, "apple", "cherri"
print(immutable_var)
print(type(immutable_var))
immutable_var[1] = "peach"
print(immutable_var)   # показывает ошибку: объект не поддерживает команду, т.е. неизменяемый
