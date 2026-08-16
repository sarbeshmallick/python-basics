

# Print all multiples of 3 from 1 to 50 but skip 15 




for i in range(1,51):
  if (i == 15):
    continue 
  if (i % 3 == 0):
    print(i)




3
6
9
12
18
21
24
27
30
33
36
39
42
45
48
