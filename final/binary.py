with open("test.bin", "wb") as f:
    f.write(b"hello world")

print("Binary file created successfully.")
with open("test.bin", "rb") as f:
    data = f.read()
    print(data)