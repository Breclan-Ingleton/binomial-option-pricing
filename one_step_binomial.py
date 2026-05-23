# One-step binomial option pricing model

S0 = 100      # initial stock price
u = 1.1       # up factor
d = 0.9       # down factor
K = 100       # strike price
r = 0.05      # risk-free rate per period

S_up = S0 * u
S_down = S0 * d

call_up = max(S_up - K, 0)
call_down = max(S_down - K, 0)

put_up = max(K - S_up, 0)
put_down = max(K - S_down, 0)

q = (1 + r - d) / (u - d)

call_price = (q * call_up + (1 - q) * call_down) / (1 + r)
put_price = (q * put_up + (1 - q) * put_down) / (1 + r)

print("One-step binomial option pricing")
print()
print("Stock price up:", S_up)
print("Stock price down:", S_down)
print()
print("Risk-neutral probability:", q)
print()
print("European call price:", call_price)
print("European put price:", put_price)
