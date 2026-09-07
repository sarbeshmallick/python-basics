

# the default tax percent is 10 but if user can enter dynamic rate to know final prices



def calculate_price(price, tax=10):
  gst = price + (price * tax/100)
  return gst 


print(calculate_price(100))

print(calculate_price(100, 20))


