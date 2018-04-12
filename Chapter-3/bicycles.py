bicycles = ['trek', 'cannondale', 'giant', 'specialized', 'cervelo', 'canyon', 'diamondback']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# Index positions start at 0, not 1
print(bicycles[1])
print(bicycles[3])
# The negative starts backwards at the end of the list
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

message = "My first bicycle was a " + bicycles[-1].title() + "."
print(message)

