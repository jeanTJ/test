def simple_hash(text,modulo):
    ascii_sum = sum(ord(char) for char in text)
    hash_value = ascii_sum % modulo
    return hash_value

#exemple d'utilisation
text = 'Bonjour'
modulo = 10
print(f"le hashage de text avec modulo {modulo} est : {simple_hash(text, modulo)}")
text2 = 'roujnoB'
print(f"le hashage de text2 avec modulo {modulo} est : {simple_hash(text2, modulo)}")

def improved_hash(text, modulo):
    ascii_sum = sum((i+1) * ord(char) for i, char in enumerate(text))
    #enumerate() permet d'iterer une sequence tout en ayant simultanement s l'index de chaque element
    #en d'autre terme retourne l'index d'un element et cet element
    # ord() retourne la valeur ascci d'un caractere
    return ascii_sum % modulo

#exemle
text2 = 'abc'
text3 = 'cab'

print(f"Hash pour {text2} : {improved_hash(text2, modulo)}")
print(f"Hash pour {text3} : {improved_hash(text3, modulo)}")
    