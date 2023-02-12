# The Multi-Armed Bandit problem

### Scenario 1: (Understanding decision making under uncertainty).

To properly understand the concept of decision making under uncertainty, let's assume a simple scenario. Assume you walk into a coffee house you have never been to. Think about the process of choosing what flavour of coffee to order. As you have no prior information about how different flavors of coffee taste like (at this coffee house), there is no real advantage of choosing one flavor over another. This process of making decisions with little (or no) prior information about the outcomes of known actions is termed as “Decision making under uncertainty.” [[1]](https://mitpress.mit.edu/9780262029254/)

This means choosing any flavour of coffee would be a new experience. In other words, called **exploring** coffee flavors. However, this might result in a bad choice (what if you ordered a flavour and didn’t like it at all?). At this point you decide turn to the ever so friendly waiter and try to gather some information about the coffee flavors (collecting **data** to make a decision). The waiter replies “Flavour A is the most-liked. You might like it the best”. In other words, Flavour A is a **recommendation** based on previous customer feedback (data) and not a decision. You proceed with the suggestion of waiter and decide to order flavour A. In other words, you decided to **exploit** the prior information and made a **greedy** decision. (These terms will start making sense soon as they are meant to set-up for terminology later.) Let’s say you really liked the Flavour A and return back to the coffee house after a couple of days. Think about the same process of choosing what to order. Do you go with your current best choice (Flavour A) or ‘explore’ more flavors? There might be a better flavour, you might not know!

## Applications of Decision making under uncertainty.

The above concept of decision making under uncertainty can be encountered across multiple domains. For example, when a new user arrives at a website, he is shown certain ads. The recommendation agent (displaying the ads) is aimed at picking an ad that would maximize the click through rate. (CTR)

$$\text{CTR} =\frac{\text{Number of clicks}}{\text{Total number of impressions}}$$

**Dynamic Pricing**: Fast-moving Consumer Goods (FMCG) is a domain with a large quantity of perishable goods. A seller must understand the change in demand for such products at regular intervals and adjust prices to maximize sales every day. This is an interesting problem from the seller point of view as there would be limited prior information to find the best possible promotion strategy to maximize the sales. This category falls under Trade Promotion Optimization. For example, would \$9.99 lead to more sales than \$10? What dates are the best to reduce (or) increase prices to maximize sales while minimizing promotional cost?


**Portfolio Optimization**: Portfolio optimization is based on Modern Portfolio Theory (MPT). The MPT is based on the principle that investors want the highest return for the lowest risk. To achieve this, assets in a portfolio should be selected after considering how they perform relative to each other, i.e.; they should have a low correlation. The agent must dynamically adjust the weights of each stock to yield maximum overall returns by choosing the best combination of stocks to be invested.

## Formalizing decision making under uncertainty into the Multi-Armed Bandit problem.

Multi-Armed Bandits (MAB) unify all the above-mentioned examples by providing a simple but very powerful framework of algorithms that make decision over time under uncertainty. [[2]](https://arxiv.org/pdf/1904.07272.pdf) In the basic version, MAB setup has K possible actions to choose from, a.k.a. arms, and T rounds. In each round the algorithm chooses an arm and collects a reward for this arm. The reward is drawn independently from some distribution (generally uniform) which is fixed but not known to the algorithm. Essentially, the goal of the solution is to maximize the overall reward (by choosing from K possible actions) in the least amount of rounds or regret (defined as the number of times suboptimal bandit is pulled).

**Definition**: Simplified version of MAB (a.k.a. Stochastic Bandits)

**Parameters**: K arms, T rounds (both known); reward distribution $\mathcal{D}_a$ for each arm $a$ (unknown).

In each round $t \in [T]$:
1. Algorithm picks some arm $a_t$.
2. Reward $r_t \in [0, 1]$ is sampled independently from the distribution $\mathcal{D}_a$, $a=a_t$.
3. Algorithm collects reward $r_t$, and observes nothing else.

## Diving deep into the MAB problem.

Having formulated a formal definition for the basic version of MAB, let’s understand the characteristics of an MAB problem and the reasons that make MAB a difficult problem to solve.

### Scenario 2: Explaining the intuition behind decision making under uncertainty.

Imagine you walk into a casino and see two slot machines in front of you. For the sake of simplicity, let’s assume each slot machine yields either a reward of \$0 or \$1. How would one choose between these slot machines? At this point there no real advantage of choosing one slot machine over the other because of no prior information. This makes any choice equivalent.

**Let’s assume, you chose slot 1 and lost**. At this point we have some information about slot 1 but have no information about slot 2. Think about which slot machine would you pick in the second try and why? Our gut says to pick slot 2 right? This is partly because of probability.

$$\text{P(success)} =\frac{\text{Number of successful events}}{\text{Total number of events}}$$

For slot 1 $\rightarrow$ P(success)=0

For slot 2 $\rightarrow$ P(success)=undefined

Our gut says that somehow 'undefined' is better than 0 and we want to explore the other slot machine, although you cannot compare them numerically. Let’s say you picked slot 2 and won. Which one do we play next? We would pick slot 2, as P(2) =1 and P(1) = 0. In terms of probability, these estimates are what we call **Maximum likelihood estimates** and the process of picking the slot machine with maximum likelihood is called **Greedy approach**.

### Statistical approach towards choosing slot machines:

Let's take a step back and think if there is something wrong in choosing slots using the greedy method. Consider we played slot machine 2 ten times and we got only 1 reward. At this point P(2) is slightly greater than 0 while P(1) is still 0. At this point there would be more disagreement about which slot machine to choose. What is the intuition behind choosing a slot machine even if the probability estimates suggest otherwise? Is there a way to algorithmically model this intuition?

A statistician would suggest that the **correct** way to approach the slot machines is to decide how many data points to collect before walking into the casino. This would help decide the [statistical power](https://machinelearningmastery.com/statistical-power-and-power-analysis-in-python/#:~:text=statistical%20power%20is%20the%20probability%20that%20a%20test,reject%20a%20false%20null%20hypothesis.&text=The%20higher%20the%20statistical%20power,when%20there%20is%20an%20effect) and the [effect size](https://en.wikipedia.org/wiki/Effect_size#:~:text=In%20statistics%2C%20an%20effect%20size,based%20estimate%20of%20that%20quantity.&text=Effect%20sizes%20complement%20statistical%20hypothesis,%2C%20and%20in%20meta%2Danalyses) of the experiment. However, one major question here is that ‘How do you know the effect size without playing the machines?’

Let’s say you decided to play each machine 10000 times. After 5000 pulls, slot machine 1 has won 3 times and slot machine 2 won 4000 times, but you cannot stop the experiment as it would invalidate the results from a statistical point of view. We must play each slot 10,000 times. This would result in the loss of several coins just to understand the reward approximation by slot machines. This is the major reason why statistical testing cannot be used to solve the MAB problem.

### Adaptation and the Explore-Exploit dilemma.

We need to formulate an algorithm that can adapt to the recent findings (just like our intuition). In the subsequent sections, a mathematical explanation and an algorithmic implementation of this intuition will be explained.

While modelling this intuition, we have two opposing forces:

1. To be a good statistician and collect as much data as possible (exploration)

2. Pick the machine with highest probability estimate (exploitation)

These two forces of exploration and exploitation oppose each other. We want to achieve maximum reward while picking the slot machines, yet we cannot calculate their true probability estimates without exploring. Everytime we explore a sub-optimal slot machine, we sacrifice the best reward for better accuracy in probability estimates. Hence, exploration and exploitation are at odds with each other and cause a dilemma while making a decision. This is called the **explore-exploit dilemma**.

The next article talks about the approaches to solve the explore-exploit dilemma.

# References
1. https://mitpress.mit.edu/9780262029254/
2. https://arxiv.org/pdf/1904.07272.pdf
