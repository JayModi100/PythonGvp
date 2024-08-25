# Print a Fibonacci 

def createFibonacci(noOfFibonacci):
    fibonacciSeriesList = ['A','B']
    while len(fibonacciSeriesList) < noOfFibonacci:
        nextString = fibonacciSeriesList[-1]+fibonacciSeriesList[-2]
        fibonacciSeriesList.append(nextString)

    return fibonacciSeriesList



noOfFibonacci = int(input("Enter length of Fibonacci series : "))
fibonacciList = createFibonacci(noOfFibonacci)
print(fibonacciList)