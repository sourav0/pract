a=5
def br():
    global a
    a=12
    print(a)
def pr():
    global a
    a=12
    print(a)
print(a)
br()
pr()
print(a)