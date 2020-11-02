def move(comms, index):
    #global pointer
    comm = comms[index]
    if comm == "LEFT":
        pointer -= 1
    elif comm == "RIGHT":
        pointer += 1
    else:
        new_idx = int(comm[-1]) - 1
        return move(comms,new_idx)

pointer = 0
tcase = int(input())
for case in range(tcase):
    #pointer = 0
    steps = int(input())
    comms = []
    for step in range(steps):
        comm = input()
        comms.append(comm)
    for comm in range(steps):
        move(comms, comm)
    print(pointer)
    pointer = 0
