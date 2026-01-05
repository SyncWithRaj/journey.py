def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()

user2 = infinite_chai()

for _ in range(10):   # Upper loop is infinite loop so from here you can control it using generators
    print(next(refill))

for _ in range(6):
    print(next(user2))

## here is we use 2 for loops or say refill chai for 2 users then first suer get refill  10 tiles and after then only user2 have chance to refill it's cup