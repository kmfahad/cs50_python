n = input("File name: ").lower()
a = n.endswith(('.gif', '.jpg', '.jpeg', 'png'))

if n.endswith(('.gif', '.jpg', '.jpeg', 'png')):
    print(f"images/{n.split('.')[-1]}")
elif n.endswith(('.pdf', '.zip')):
    print(f"application/{n.split('.')[-1]}")
else:
    print("application/octet-stream")


