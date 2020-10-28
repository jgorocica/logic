def draw_grid(n, m):
    
    # Get the Right side 
    if (n == m and n % 2 != 0 and m % 2 != 0):
        return 'R'
    # Get the Left side
    elif (n == m and n % 2 == 0 and m % 2 == 0):
        return 'L'
    # Get the Down side 
    elif (n > m and m == 1):
        return 'D'
    else: 
    # Get the Up Side (Where m > n)
        return 'U'

def get_cases():
    print(" **** P R O G A M A  D E  L Ó G I C A **** ")
    cases = int(input('Ingrese el número de casos... '))
    
    for i in range(cases):
        n = int(input("Ingrese el valor de n: "))
        m = int(input("Ingrese el valor de m: "))
        print(draw_grid(n, m))

if __name__ == '__main__':
    get_cases()