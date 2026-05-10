# Password generator project

## Understanding concepts

### Modules

A module is a just a file that contains reusable code.

#### 1. `re` module

 Helps us to search for patterns in a text and it is imported as shown below.

```python
import re
```

Mathematically, a function like `re.findall(r"\b", your_text)` literally means getting a subset from an entire set.

Example:

Check if 1 is a subset in the digits set.

$$
"1" \in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
$$

Python code:

```python
import re

re.findall(r"\b", ["1", "1", "2", "3"])
```
#### 2. `secret` module

This module generates cryptographically secure random values. 

The `random` module, basically generates a general random output.

A password generator need to have $P(CorrectGuess)$ being very close to zero.

Finally, secrets minimizes randomness quality.

#### 3. `string` module

This module provides character groups such a digits, lower and upper case letters, and symbols.


### Functions

A function takes in inputs and maps a transformed version of it as an output. In Python function hides the complex implementation behind simple interface.

A function has parameters. Parameters are the input of a function. One can actually set default values for any parameter they want but they have to follow an order. Default ones comes first then the rest follow.

Example:

$$
f(x) = 2x
$$

Programmatically we have:

```python
def f(x):
    return x * x
```

The input value $x$ is transformed by squiring it. Then, the result is returned as output.

*Abstraction* is hiding the complexity of a problem and showing only what the user wants/needs at the moment.


