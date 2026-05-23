# Binomial Option Pricing

This project uses simple Python models to price European options using binomial stock price trees.
This project is intended to build intuition for how simple option pricing models work before moving on to more advanced financial mathematics.

## Files

- `one_step_binomial.py` — prices a European call and put option using a one-step binomial model.
- `two_step_binomial.py` — prices a European call and put option using a two-step binomial tree with backward induction.
- `multi_step_binomial.py` — prices a European call and put option using a reusable multi-step binomial pricing function.

## One-Step Binomial Model

The file `one_step_binomial.py` models a stock that can move up or down over one period.

It calculates the payoff of a European call and put option in each state.

It then uses the risk-neutral probability to calculate the fair option price.

## Two-Step Binomial Model

The file `two_step_binomial.py` extends the model to two periods.

It calculates option payoffs at the final stock prices, then works backwards through the tree to find the option price at time 0.

## Multi-Step Binomial Model

The file `multi_step_binomial.py` generalises the model to any number of steps.

It uses a function to calculate European call and put prices using backward induction.
