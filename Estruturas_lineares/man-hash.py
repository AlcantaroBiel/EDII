import hashlib

msg = "Olá mundo!"
hash_obj =  hashlib.md5(msg.encode())
print(hash_obj.hexdigest())