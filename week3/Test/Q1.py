# What is the purpose of __init__?
# Explain when it runs, what self represents,
# and why forgetting self causes Python to complain in a very passice-aggressive way.

# When the function runs, __init__ is processed evey time. CLASS!
# It's for initialize the settings.
# We need "self" because python can't understand what is __init__. 
# It is a function and not user defined name.

# __init__ is a special method
# It runs automaticallywhen a new object is created from a class
# When u = User("Alice") process, python roughly call this:
# 1. Create a new empth User object
# 2. Call User.__init__(u, Alice)

# We need self beause that makes self.name first, this means to create u.name

