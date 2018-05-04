import re
shoppingListRegex = re.compile(r'\d+\s\w+')
list: str = input()
mo = shoppingListRegex.search(list)
print(mo.findall())
