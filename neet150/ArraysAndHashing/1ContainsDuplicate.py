def ContainDuplicates(list1):
  seen = set()

  for num in list1:
    if num in seen:
      return True
    else:
      seen.add(num)
  return False


print(ContainDuplicates([1, 2, 3, 4]))

