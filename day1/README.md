# Advent of Code 2025 - Day 1

## Interesting findings

- Negative modulo in Python behaves similarly to wrapping around in a circular list.
- Negative floor division rounds, resulting in a larger number numerically.
- Negative floor division is consistent with negative modulo in
that `(a // b) * b + (a % b) == a` always holds true.
