
import sys as p__sys


items = p__sys.path
value = items.pop(0)
items.append(value)
del p__sys


from source.server import function


function()
