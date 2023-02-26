#!/usr/bin/env python
# coding: utf-8

# # The Bellman Equation
# 
# Let's discuss value functions for a second. One useful way to think about these values functions is the the form of probabilistic trees.
# 
# Consider a biased coin with $\text{P(heads)} = 0.6$ and $\text{P(tails)} = 0.4$. Let the rewards for tails be 0 and reward for heads = 1. The root note represents the current state. From the below graph its clear.
# 
# ```{figure} /imgs/rl/bellman1.PNG
# 
# Simple tree to calculate expected reward
# 
# ```
# 
# The Expected reward for the above scenario will be $0.6 \times 1 + 0.4 \times 0 = 0.6$. The expected reward is the weighted sum of all possible rewards given the current state. Note that this is true for any tree with the child nodes being all possible states from current state and the edges representing the transition probability from current state to each of the child nodes (states).
# 
# $$
# \begin{align}
# E(X) = \sum_x xp(x)
# \end{align}
# $$
# 
# We can extend this concept even further. In the above figure, we have considered a simple scenario with just one level of child nodes. For example, in games like tic-tac-toe, the game is not over at just one time stamp and each child node is yet another tree with further child nodes of their own. In other words this leads to `recursion`, with each child of a tree being a tree in itself.
# 
# **Can we use this property to find a generalized formula for calculation of expected rewards?**
# 
# $$
# \begin{align}
# G_1 = 
# \end{align}
# $$
# 
# 
# 

# In[ ]:




