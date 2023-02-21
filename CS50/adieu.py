import inflect
p = inflect.engine()

list = []
while True:
    try:
        name = input()
        list += [name]
    except KeyboardInterrupt:
        mylist = p.join((list),final_sep='')
        print(mylist)
        break