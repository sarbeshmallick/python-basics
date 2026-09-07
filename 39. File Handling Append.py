


# Prblm stat-
# Using your existing output.txt, write Python code that adds:
# Pineapple
# Watermelon
# to the end of the file without deleting Apple, Banana, Orange and Mango.





with open("output.txt", "a") as file:
  file.write("Pineapple\n")
  file.write("Watermelon\n")



