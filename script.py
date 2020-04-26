#standard ground shipinng
def ground_shipping_cost(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else :
    price_per_pound = 4.75
  return 20 + (weight * price_per_pound)
print(ground_shipping_cost(8.4))

#premium ground shipping
premium_ground_shipping = 125.00


#Drone Shipping
def drone_shipping_cost(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else :
    price_per_pound = 14.25
  return  (weight * price_per_pound)
print(drone_shipping_cost(1.5))



#cheapest shipping method
def print_cheapest_shipping_method(weight):
  ground = ground_shipping_cost(weight)
  premium = premium_ground_shipping
  drone = drone_shipping_cost(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method ="premium ground"
    cost = premium
  else:
    method ="drone"
    cost = drone
    
  
  print(
    "The cheapest option available is $%.2f with %s shipping"
      % (cost, method)
  )
  

print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.5)

  
    

  
  




