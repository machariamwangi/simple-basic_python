import converters
from converters import kg_to_lbs
from utils import  find_max

numbers = [10, 3, 6, 2]
find_max(numbers)


kg_to_lbs(100)
print(converters.kg_to_lbs(70))
print("new ans:",find_max(numbers))
print("no two", max(numbers))