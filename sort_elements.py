#The ultimate collection of numbers
# Continue statement to skip the execution on the else statement
# Ways to sort element 

items=[1,5,7,8,"Free","Spam","False",89,90,11,"Python"]
refined_items=[]
for item in items:
    if type(item) != int:
        continue
    else:
        refined_items.append(item)

print(refined_items)

   
