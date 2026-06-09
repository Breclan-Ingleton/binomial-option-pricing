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

## Parameters

The main multi-step model uses the following parameters:

| Parameter | Meaning |
|---|---|
| `S0` | Initial stock price |
| `K` | Strike price of the option |
| `r` | Risk-free rate per time step |
| `u` | Up factor for the stock price |
| `d` | Down factor for the stock price |
| `N` | Number of time steps in the binomial tree |
| `option_type` | Either `"call"` or `"put"` |

## Risk-neutral probability

The multi-step model uses the risk-neutral probability

```python
q = (1 + r - d) / (u - d)
```
This is not meant to be the real-world probability that the stock price goes up.

Instead, it is a mathematical probability used for no-arbitrage pricing. It lets the model calculate the discounted expected future option value at each step of the tree.

## Example results

Using the example parameters in the scripts, the models give:

| File | European call price | European put price |
|---|---:|---:|
| `one_step_binomial.py` | 7.14 | 2.38 |
| `two_step_binomial.py` | 10.71 | 1.42 |
| `multi_step_binomial.py` | 22.81 | 1.16 |

These values are different because each file uses a different number of time steps. The one-step and two-step files are mainly explanatory, while `multi_step_binomial.py` generalises the method to any number of steps.
