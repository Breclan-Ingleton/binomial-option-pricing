# Binomial Option Pricing

This project uses simple Python models to price European options using binomial stock price trees.

## Files

- `one_step_binomial.py` — prices a European call and put option using a one-step binomial model.
- `two_step_binomial.py` — prices a European call and put option using a two-step binomial tree with backward induction.

## One-Step Binomial Model

The file `one_step_binomial.py` models a stock that can move up or down over one period.

It calculates the payoff of a European call and put option in each state.

It then uses the risk-neutral probability to calculate the fair option price.
