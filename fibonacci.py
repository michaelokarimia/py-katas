class Fibonacci:

    @staticmethod
    def fibonacci(n):

        if n == 0:
            return 0

        if n == 1:
            return 1

        return (Fibonacci.fibonacci(n-1) + Fibonacci.fibonacci(n-2))

    def run(self):

        strInt = input("Enter the Fibonacci number\n")

        n = int(strInt)

        print(Fibonacci.fibonacci(n))