#function
def number():
    #this func get number and show factorial
    x = int(input('enter the number:'))
    javab = 1
    for a in range(1 , x + 1):
        javab = javab * a
    print(javab)
    return(again())

def again():
    #this func ask for use factorials function again
    do_again = input('Do you want to try again?___<y> for yes and <n> for no:')
    if do_again == 'y':
        number()
    elif do_again == 'n':
        print ('< Goodby my friend >')
    else:
        again()
number()
