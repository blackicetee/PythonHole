def implication(A, B):
    if A and B:
        return True
    elif A:
        return False
    elif B:
        return True
    elif not A and not B:
        return True
    else:
        print('Error')

print('Case_1: A = true and B = true \nResult of A => B = {}'.format(implication(True,True)))
print('Case_2: A = true and B = false \nResult of A => B = {}'.format(implication(True,False)))
print('Case_3: A = false and B = true \nResult of A => B = {}'.format(implication(False,True)))
print('Case_4: A = false and B = false \nResult of A => B = {}'.format(implication(False,False)))
