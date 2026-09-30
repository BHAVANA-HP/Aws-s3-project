import hashlib

# Hash of file1
with open("file1.txt", "rb") as f:
    hash1 = hashlib.sha256(f.read()).hexdigest()

# Hash of file2
with open("file2.txt", "rb") as f:
    hash2 = hashlib.sha256(f.read()).hexdigest()

print("File 1 hash:")
print(hash1)

print("\nFile 2 hash:")
print(hash2)

if hash1 == hash2:
    print("\nFiles are identical ")
else:
    print("\nFiles are different / modified ")