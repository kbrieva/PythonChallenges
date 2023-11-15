class Category:
  def __init__(self, categories):
    self.category = categories
    self.ledger = []
    self.total = 0
    
  def __repr__(self):
    s = f"{self.category:*^30}\n"
    for item in self.ledger:
      # s += f"{item['description'][:23]} {item['amount']:>{30-len(item['description']):}.2f}\n"
      s += f"{item['description'][:23]}".ljust(24) + f"{item['amount']:.2f}" + "\n"

      
    # s += "-" * 30
    s += f"Total: {self.total:.2f}"
    return s
  
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.total += amount

  def check_funds(self, amount):
    if amount <= self.total:
      return True
    else:
      return False

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
     
      self.ledger.append({"amount": -amount, "description": description})
      self.total -= amount
      return True
    else:
      return False
    
  
  def transfer(self, amount, categories):
    if self.check_funds(amount):
        self.ledger.append({"amount": -amount, "description": f"Transfer to {categories.category}"})
        self.total -= amount
        categories.deposit(amount, description= f"Transfer from {self.category}")
        return True
    else:
      return False
    
  def get_balance(self):
    return self.total


# def create_spend_chart(categories):
  
#   chart = "Percentage spent by category\n"
#   names = []
 
#   spendings = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
#   total_spent = sum(spendings)
#   percentages = [(spent / total_spent) * 100 if total_spent > 0 else 0 for spent in spendings]
#   for cat in categories:
#     names.append(cat.category)
    
     
    
#   print("This is it", total_spent)   

#   for num in range(100, -1, -10):
#     chart += f"{str(num)+'|':>4}"
#     for item in percentages:
#       if item >= num:
#         chart += " o "
#     chart += "\n"
#   # chart += f"    {2 * '-----'}\n"
#   chart += "    -" + "---" * len(categories) + "\n"

 
#   for i in range(max(map(len, names))):
#     chart += "     "
#     chart += ('  '.join(name[i] if i < len(name) else ' ' for name in names)) + '\n'
    

#   return (chart)

def create_spend_chart(categories):
  chart = "Percentage spent by category\n"
  spendings = [sum(item['amount'] * -1 for item in category.ledger if item['amount'] < 0 ) for category in categories]
  total_spent = sum(spendings)
  # percentages = [(spent / total_spent) * 100 if total_spent > 0 else 0 for spent in spendings]
  percentages = [int(spent / total_spent * 100) if total_spent > 0 else 0 for spent in spendings]
  

  print(total_spent)
  for i in range(100, -1, -10):
      chart += str(i).rjust(3) + "| "
      for percent in percentages:
          chart += "o" if percent >= i else " "
          chart += "  "
      chart += "\n"
  
  chart += "    -" + "---" * len(categories) + "\n"
  
  max_len = max(len(category.category) for category in categories)
  for i in range(max_len):
      chart += "     "
      for category in categories:
          chart += category.category[i] if i < len(category.category) else " "
          chart += "  "
      if i < max_len - 1:
          chart += "\n"
  
  return chart.rstrip("\n")



food = Category("Food")
entertainment = Category( "Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
# food.withdraw(123.55)
# food.withdraw(135.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(business)
print(food)
print(entertainment)

print(create_spend_chart([business, food, entertainment]))
  # print(tt)
  # print(food, auto)




# auto = Category("auto")
# food = Category("Food")
# clothing = Category("Clothing")
# food.deposit(1000, "initial deposit")
# food.withdraw(100, "groceries")
# food.withdraw(10, "groceries")
# food.withdraw(200, "groceries")
# food.withdraw(30, "groceries")
# food.transfer(660.01, auto)
# auto.deposit(1000, "deposit")
# auto.withdraw(60)
# auto.withdraw(70)
# auto.withdraw(80)
# auto.withdraw(90)
# clothing.deposit(1000, "deposit")
# clothing.withdraw(60)
# clothing.withdraw(70)
# clothing.withdraw(80)
# clothing.withdraw(90)


# # print(food.total)

# create_spend_chart([food, clothing, auto])


# print(food)
# print(auto)
# food.withdraw(15.89, "restaurant and more food for dessert")

# clothing = Category("Clothing")
# food.transfer(500, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
# # print(food.check_funds(10))
# print(food)
# print(auto)
# print(clothing)



# Print each character vertically
# entertainment = Category('entertainment')
# food = Category("food")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# print(food)