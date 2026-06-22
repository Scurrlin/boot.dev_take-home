# List Comprehensions

A list comprehension is an easy way to create a new list from an existing list by applying a specific transformation to each item. Instead of writing an empty list and a `for` loop, you can do it all in one line.

Here's the long way to create a new list of doubled numbers:

```python
doubled = []
for num in nums:
    doubled.append(num * 2)

# nums = [1, 2, 3, 4, 5]
# doubled = [2, 4, 6, 8, 10]
```

And here's the same thing using list comprehension:

```python
doubled = [num * 2 for num in nums]

# nums = [1, 2, 3, 4, 5]
# doubled = [2, 4, 6, 8, 10]
```

Both examples create the exact same list, but using list comprehension is generally preferred for simple transformations (like doubling numbers).

## Filtering With a Condition

You can also add an `if` condition to the end of a list comprehension to only keep some of the items. The example below creates a new list containing only numbers bigger than 100:

```python
big_numbers = [num for num in nums if num > 100]

# nums = [14, 260, 35, 42, 510]
# big_numbers = [260, 510]
```

Any item where the condition is `False` is skipped, so the new list only contains the filtered items.

You can even transform *and* filter at the same time! The example below filters a list of names and creates a new list of capitalized names that contain more than 5 letters.

```python
big_names = [name.upper() for name in names if len(name) > 5]

# names = ["Aragorn", "Gimli", "Legolas", "Boromir"]
# big_names = ["ARAGORN", "LEGOLAS", "BOROMIR"]
```

Remember, a list comprehension *always* creates a brand new list. It never changes the list you started with.

## Assignment

A bug in the latest Fantasy Quest patch is tripling every hero's level. This means your casual friends will finally be able to join you in the new raid!

The Fantasy Quest party screen unfortunately doesn't show bugged character stats, so you'll need to add a new function to calculate the increased value. Each hero is a tuple of name and level, like `("Gojo", 90)`.

Let's finish the `get_new_levels(heroes, min_level)` function using a single list comprehension.

1. Loop over each `hero` in `heroes`.
2. Keep only the heroes whose tripled level (`hero[1] * 3`) is greater than or equal to `min_level`.
3. For each hero you keep, create a tuple of their name and tripled level.
4. Return the new list of hero tuples.

For example, `get_new_levels([("Gojo", 90), ("Yuji", 45)], 80)` should return:

```python
[("Gojo", 270), ("Yuji", 135)]
```

because both Gojo and Yuji meet the raid's level requirement.

The `pass` keyword tells Python to do nothing. You'll need to replace it with your own code.
