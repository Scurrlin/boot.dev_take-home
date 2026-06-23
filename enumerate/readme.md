# Enumerate

Most of the time when you loop over a list of items, you're trying to access the value of each item.

```python
for item in items:
    print(item)

# item1
# item2
# item3
```

However, sometimes the position of the item matters too. If you want to get both, you'll need to manually set the range for your loop and *then* use each index to look up its corresponding value:

```python
for i in range(0, len(items)):
    print(i, items[i])

# 0 item1
# 1 item2
# 2 item3
```

Surely there must be a simpler way to do this, right? Of course there is!

The `enumerate()` function gives you a clean, memory efficient way to get both the index *and* value of each item by using a counter during the loop to keep track of the indices.

```python
for i, item in enumerate(items):
    print(i, item)

# 0 item1
# 1 item2
# 2 item3
```

The two previous loops print the same index/value pairs, but the second version is easier to read and less prone to errors.

## Counting From Any Number

Since lists start at index `0` by default, `enumerate()` also starts counting at `0`. We don't really mind this in programming, but magical quests and instruction manuals would probably look pretty strange starting at step `0`.

This can easily be changed by passing a `start` value to `enumerate()`. The `start` value can be any integer and only changes what number the counter actually *starts* with, not the list itself.

In this example, the first item is numbered `1` instead of `0`.

```python
for i, item in enumerate(items, start=1):
    print(i, item)

# 1 item1
# 2 item2
# 3 item3
```

## Assignment

Ever since the recent Secret Shop promotion, Daginald Whimsby's Fantastiporium has been absolutely swamped... so much so that the bearded bard can no longer rely on his wits alone to account for his inventory. Much to his chagrin, Tilda's finally been able to talk him into making a numbered list of his instruments.

Let's help him out by finishing the `numbered_inventory(items)` function. It takes a list of item names and returns a new list of numbered strings. The function already creates an empty list called `numbered_items`.

1. Use `enumerate()` to loop over `items`, starting the count at `1`.
2. For each item, create a string containing its number, followed by `. `, then the item name.
3. Append each numbered string to `numbered_items`.
4. Return `numbered_items`.

For example, `numbered_inventory(["Lute", "Flute", "Harp"])` should return:

```python
["1. Lute", "2. Flute", "3. Harp"]
```

The `pass` keyword tells Python to do nothing. You'll need to replace it with your own code.
