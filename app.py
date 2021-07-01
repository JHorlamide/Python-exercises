# Imports from modules
import modules
from modules import kg_to_lbs

# Imports from e_commerce
import e_commerce.shipping
from e_commerce.shipping import calculate_shipping

# Using functions from modules
print(modules.lbs_to_weight(40))
print(kg_to_lbs(40))

# Using functions from e_commerce
e_commerce.shipping.calculate_shipping()
calculate_shipping()