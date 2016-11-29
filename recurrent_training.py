def iteration(steps):
    if steps > 0:
        print(steps)
        return iteration(steps - 1)
    else:
        print(steps)

iteration(10)

