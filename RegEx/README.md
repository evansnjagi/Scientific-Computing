# RegEx Note
---  

RegEx(also, regular expressions) is a sequence of characters that defines a search.

A *pattern* is a rule that defines a SET of strings(a whole category of strings).

Building the connection:
    
1. Math connection
    
    In maths, we use set builder to represent pattern in a set.
    
    For example, we can represent a set of all positive integers as shown below:

    $$\{x \in \mathbb{Z} | x > 0\} \rightarrow \{1, 2, 3, 4, 5, ...\}$$
2. RegEx

A good example of a string is: a string of one or more digit written as `r"\d+"`.


## Match group

## \d 

## The {n} quantifier

## The + quantifier

## The * quantifier

The (*) quantifier is only used when things are optional but repeatable when present. 

Mathematically it can be represented as `r"\d*"` $\rightarrow$ $[0, \infty)$

The best use case is when you are working on a feature, from you dataset, that has price values in it. The price may or may not have cents. 

Example dataset:

| Id | Price  | Description| 
| -- | -----  | ------|
|  1 | KES 500| Whole Number|
| 2 | KES 500.75 | Has Two decimals|
|  3 | KES 1200.5| Ha one decimal|

You can not use `\d +` as your pattern, because sometimes the decimal is not there.

Syntax example:

```python
Loop p items:
    match = re.search(r"\d\.\d*", p)
```

To get the script run the command below:

```bash
python  mquantifier.py
```

To check the content run:

```bash
code mquantifier.py
```
---
Footnote 

This document contains my own handwritten note. Inside, it may have grammatical, structural, or even coding error. Check important information before using it for purposeful-result driven learning.

@Evans Karago - Deep Learner.

---