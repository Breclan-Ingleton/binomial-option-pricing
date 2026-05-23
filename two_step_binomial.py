# Two-step binomial option pricing model

S0 = 100
u = 1.1
d = 0.9
K = 100
r = 0.05

q = (1 + r - d) / (u - d)

# Stock prices after two steps
S_uu = S0 * u * u
S_ud = S0 * u * d
S_dd = S0 * d * d

# Call payoffs at final time
call_uu = max(S_uu - K, 0)
call_ud = max(S_ud - K, 0)
call_dd = max(S_dd - K, 0)

# Put payoffs at final time
put_uu = max(K - S_uu, 0)
put_ud = max(K - S_ud, 0)
put_dd = max(K - S_dd, 0)

# Work backwards one step
call_up = (q * call_uu + (1 - q) * call_ud) / (1 + r)
call_down = (q * call_ud + (1 - q) * call_dd) / (1 + r)

put_up = (q * put_uu + (1 - q) * put_ud) / (1 + r)
put_down = (q * put_ud + (1 - q) * put_dd) / (1 + r)

# Work backwards to time 0
call_price = (q * call_up + (1 - q) * call_down) / (1 + r)
put_price = (q * put_up + (1 - q) * put_down) / (1 + r)

print("Two-step binomial option pricing")
print()
print("Risk-neutral probability:", q)
print()
print("European call price:", call_price)
print("European put price:", put_price)
