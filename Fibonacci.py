class Solution:

    def nthFibonacciUtil(self, n, dp):
        # Base case
        if n <= 1:
            return n

        # Check if the result is
        # already in the dp table
        if dp[n] != -1:
            return dp[n]

        # calculate Fibonacci number
        # and store it in dp table
        dp[n] = self.nthFibonacciUtil(n - 1, dp) + self.nthFibonacciUtil(
            n - 2, dp)

        return dp[n]

    def nthFibonacci(self, n: int) -> int:

        # Create a dp table and
        # initialize with -1(invalid value)
        dp = [-1] * (n + 1)
        return self.nthFibonacciUtil(n, dp)
