```python
from pwn import xor
ct = bytes.fromhex(
    "9bfdb1b2aae1e3e1aaffb3fea6b2b4fb59450d4c0d5e44434a41480d4f545948e2ffa7edeeb4b6f5a9f1e2e0aaf1e2b4a4d1a3daf89dabd3a1c9a4d7b9cef3d3757e774d267c764d61237f627e216f"
)
for c in [ct[16*i : 16*(i+1)] for i in range((len(ct)//16) + 1)]:
	for k in [chr(i).encode() for i in range(256)]:
		x = xor(c,k)
		if b'inctfj' in x or b'_' in x and b'}' in x:
			print(x.decode(), end="")
			break```
