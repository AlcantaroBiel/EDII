import hashlib

msg = "Olá mundo!"
hash_md5 =  hashlib.md5(msg.encode())
print(hash_md5.hexdigest())

hash_sha1 = hashlib.sha1(msg.encode())
print(hash_sha1.hexdigest())

hash_sha256 = hashlib.sha256(msg.encode())
print(hash_sha256.hexdigest())

hash_sha512 = hashlib.sha512(msg.encode())
print(hash_sha512.hexdigest())