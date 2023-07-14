# Contextual Value Shifter

Or `ctxvalue-shifter` for short, or `cxvshifter` for shorter.

A Python module that implements a contextual "shift" function.

## Installing

You can get Contextual Value Shifter from PyPI.

```bash
pip install ctxvalue-shifter
```

## Usage

```python
from cxvshifter import shift

# Shifting to variables
x = 5
shift(10, 'x')
print(x)
# => 10

# Shifting to a file
shift("hello", 'file', "hello.txt")

# Shifting to stdout
shift("Hello, shifting world!", 'stdout')

# Shifting to return
shift(24, 'return')
# -> 24
```

## Improper usage

```python
x = 5
shift(10, x)
# Will attempt to shift to a variable named 5
# In ctxvalue-shifter, this will result in a TypeError
```

## Questions

+ Q: **Uhhh, first off, why?**
  + A: HAHAHA, PYTHON GO WEEEEE
+ Q: **No seriously. Why make something so useless?**
  + A: Because it's fun.
+ Q: **Why does `destination` have to be string?**
  + A: That's how ~~mafia~~ Python works.
