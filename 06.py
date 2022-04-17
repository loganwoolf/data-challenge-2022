def find_the_gate(gates, craft):
  index = 0
  if craft == 'narrow':
    for gate in gates:
      if gate == 'W' or gate == 'N':
        return index
      index += 1
  if craft == 'wide':
    for gate in gates:
      if gate == 'W':
        return index
      index += 1
  return False

print(find_the_gate(
    ['w', 'n', 'W'], 'narrow'
))

print(find_the_gate(
    ['w', 'n', 'N', 'W', 'n', 'W'], 'wide'
))

print(find_the_gate(
    ['w', 'n', 'n', 'w', 'n', 'n'], 'narrow'
))

print('===========')
print(find_the_gate(
  ['w','n','n','w','N','n','w','N','N','w','n','n','w','n','n','W','W','W','W','n','n','w','n','n'], 'wide'
))
