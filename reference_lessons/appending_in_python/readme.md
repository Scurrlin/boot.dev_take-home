# Appending in Python

It's common to create an empty list then fill it with values using a loop. We can add values to the end of a list using the `.append()` method:

```python
cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']
```

## Assignment

We need to generate a unique user ID for each player in the game. An ID is just a unique number that identifies a user.

Let's finish the `generate_user_list` function. In the body of the loop, use the incrementing value `i` as unique IDs and append them to the `player_ids` list.
