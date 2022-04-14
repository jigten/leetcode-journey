# Steps to convert top-down into bottom-up

### 1. Start with a completed top-down implementation.

### 2. Initialize an array `dp` that is sized according to your state variables. For example, let's say the input to the problem was an array `nums` and an integer `k` that represents the maximum number of actions allowed. Your array `dp` would be 2D with one dimension of length `nums.length` and the other of length `k`. The values should be initialized as some default value opposite of what the problem is asking for. For example, if the problem is asking for the maximum of something, set the values to negative infinity. If it is asking for the minimum of something, set the values to infinity.

### 3. Set your base cases, same as the ones you are using in your top-down function. Recall in House Robber, `dp(0) = nums[0]` and `dp(1) = max(nums[0], nums[1])`. In bottom-up, `dp[0] = nums[0]` and `dp[1] = max(nums[0], nums[1])`.

### 4. Write a for-loop(s) that iterate over your state variables. If you have multiple state variables, you will need nested for-loops. These loops should start iterating from the base cases.

### 5. Now, each iteration of the inner-most loop represents a given state, and is equivalent to a function call to the same state in top-down. Copy the logic from your function into the for-loop and change the function calls to accessing your array. All `dp(...)` changes into `dp[...]`.

### 6.We're done! `dp` is now an array populated with the answer to the original problem for all possible states. Return the answer to the original problem, by changing `return dp(...)` to `return dp[...]`.
