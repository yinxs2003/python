f = None
try:
    f = open('WorkList/To_Do_List.todo', 'r')
    to_do_list = f.read()

finally:
    if f:
        f.close()

with open('WorkList/To_Do_List.todo', 'w') as f:
    f.write('Hello, world!')
