# shifter

A Python module that implements a contextual "shift" function.

## Usage

```python
from shifter import shift

# Shifting to variables
x = 5
shift(10, 'x')
print(x)
# -> 10

# Shifting to a file
shift("hello", 'file', "hello.txt")

# Shifting to stdout
shift("Hello, shifting world!", 'stdout')
```

## Improper usage

```python
x = 5
shift(10, x)
# will attempt to shift to a variable named 5
```
