def difference(n):
    if n<=17:
        return 17 -n
    else:
        return(n-17) * 2

print(difference(44))

'''Example Situation (Real-Life Analogy):
Imagine a rule like:

You're allowed to bring up to 17 items into a meeting.

For each extra item, you have to pay double the fee.

If you bring 20 items:

The first 17 are fine (no penalty).

The extra 3 items cost double:
Penalty = (20 - 17) * 2 = 6

It’s not about mathematics, but about a rule-based consequence.

In Short:
The difference is doubled when n > 17 to emphasize or penalize exceeding 17, making the function behave differently for values above a certain threshold.'''