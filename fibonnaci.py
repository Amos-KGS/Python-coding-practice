def fibonnacci(n):
    if n < 0:
        return None

    if n < 3:
        return 1

    return fibonnacci(n - 1) + fibonnacci(n - 2)
    

n = int(input("Enter a number to find fibonnacci: "))
print(n, 'fibonnacci is: ', fibonnacci(n))                

