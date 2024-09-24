'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def insertionSort(sList, N):
    for i in range(1,N):
        j = i-1
        temp = sList[i]
        while(j >= 1 and temp < sList[j]):
            sList[j+1] = sList[j]
            j = j-1
        
        sList[j+1] = temp




if __name__ == '__main__' :
    import random
    sList = []
    while len(sList) < 15:
        num = random.randint(0,99)
        sList.append(num)
        
    print(f'정렬 전: {sList}')
    insertionSort(sList, len(sList))
    
    print(f'정렬 후: {sList}')
