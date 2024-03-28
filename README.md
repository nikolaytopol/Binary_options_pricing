# Binary_options_pricing
Monte Carlo scheme to price binary options

To calclulate binary path independent option call option. Discounted Value of expected payoff is used.
$$C=exp(-r(T−t))*(E[max(0,ST−K)])$$
First it is necessary to obtain posible price paths of the underlying asset (Stock). To do that Euler Maruyama method is used to simulate continious geometric Brownian Motion process $$dSt=rStdt+σStdZt$$ by simulating it using equation $$St=St−Δt(1+rΔt+σ√ΔtXt)$$ where Xt is stochastic process that follows standard normal distribution.
