data = []
with open('input.txt', 'r') as file:
    for line in file:
        name, price, action = line.split()
        price = int(price)
        action = action.lower()
        if action == 'true':
            action = True
        else:
            action = False
        data.append((name, price, action))

data.sort(key=lambda x: x[0])

with open('output.txt', 'w') as file:
    for item in data:
        file.write(f"{item[0]} {item[1]} {item[2]}\n")

with open('output.dat', 'wb') as file:
    for item in data:
        name = item[0].encode('utf-8')
        size = len(name)
        file.write(size.to_bytes(4, 'little'))
        file.write(name)
        file.write(item[1].to_bytes(4, 'little'))
        file.write(int(item[2]).to_bytes(1, 'little'))

new_data = []
with open('output.dat', 'rb') as file:
    while True:
        size = int.from_bytes(file.read(4), 'little')
        if not size:
            break
        name = file.read(size).decode('utf-8')
        price = int.from_bytes(file.read(4), 'little')
        action = bool(int.from_bytes(file.read(1), 'little'))
        new_data.append((name, price, action))

new_data.sort(key=lambda x: x[1])

with open('output2.txt', 'w') as file:
    for item in new_data:
        file.write(f"{item[0]} {item[1]} {item[2]}\n")
