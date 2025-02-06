import hashlib
text = 'hello'

hash_md5 = hashlib.md5(text.encode()).hexdigest()
print(hash_md5)
text1 = 'world'
hash1_md5 = hashlib.md5(text1.encode()).hexdigest()
print(hash1_md5)

hash_sha = hashlib.sha256(text.encode()).hexdigest()
print(hash_sha)