# Multi-step binomial option pricing model

def binomial_option_price(S0, K, r, u, d, N, option_type):
    q = (1 + r - d) / (u - d)

    option_values = []

    for j in range(N + 1):
        stock_price = S0 * (u ** j) * (d ** (N - j))

        if option_type == "call":
            payoff = max(stock_price - K, 0)
        elif option_type == "put":
            payoff = max(K - stock_price, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")

        option_values.append(payoff)

    for step in range(N - 1, -1, -1):
        new_values = []

        for j in range(step + 1):
            value = (q * option_values[j + 1] + (1 - q) * option_values[j]) / (1 + r)
            new_values.append(value)

        option_values = new_values

    return option_values[0]


S0 = 100
K = 100
r = 0.05
u = 1.1
d = 0.9
N = 5

call_price = binomial_option_price(S0, K, r, u, d, N, "call")
put_price = binomial_option_price(S0, K, r, u, d, N, "put")

print("Multi-step binomial option pricing")
print()
print("Number of steps:", N)
print("European call price:", call_price)
print("European put price:", put_price)
