
# Prblm stat- 
# create a filed called numbers.txt. Put some numbers in it like 10,20,...,50
# Then write Python code that opens the file and prints its contents.


with open("numbers.txt", "r") as file:

  content = file.read()
  print(content)



  
