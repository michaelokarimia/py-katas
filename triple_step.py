class TripleStep:
    @staticmethod
    def triple_step(n):

        memo = [0] * (n + 1)

        memo[0] = 0

        memo[1] = 1

        result = TripleStep._triple_step(n,memo)

        return result

    @staticmethod
    def _triple_step(n, memo):

        if n < 0:
            return 0

        if n == 0:
            return 1

        memo[n] = TripleStep._triple_step(n-1, memo) + TripleStep._triple_step(n-2, memo) + TripleStep._triple_step(n-3, memo)

        print(memo)

        return memo[n]


    @staticmethod
    def run():

        str_in = input("Enter number of steps \n")

        n = int(str_in)

        print("There are {} possible combinations".format(TripleStep.triple_step(n)))

