
dragon_scales = 3       
scale_price = 10       

elf_tears = 5          
tear_price = 3         

cost_of_scales = dragon_scales * scale_price   
cost_of_tears = elf_tears * tear_price         
total_cost = cost_of_scales + cost_of_tears   

print("=== Potion Ingredients Bill ===")
print(f"Dragon Scales : {dragon_scales} x {scale_price} gold = {cost_of_scales} gold")
print(f"Elf Tears     : {elf_tears} x {tear_price} gold = {cost_of_tears} gold")
print(f"Total Cost    : {total_cost} gold")
