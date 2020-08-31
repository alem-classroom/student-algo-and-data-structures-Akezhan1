def linear_search(lst, to_find):
  if to_find in lst:
    i = 0
    while i < len(lst):
      if lst[i] == to_find:
        return lst[i]
      i += 1
  return -1