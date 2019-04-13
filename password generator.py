import random
a="abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ()!@#$%^&*"
passlen=15
p=" @".join(random.sample(a,passlen))
print(p)
