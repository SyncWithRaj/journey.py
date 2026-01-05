def serve_chai():
    yield "Cupt 1: Masala Chai"
    yield "Cupt 2: Ginger Chai"
    yield "Cupt 3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai))  # This provides error bcz no 4th cup there
print(chai)




"""
# GENERATOR:

- A generator is a special kind of function that produces values one at a time, instead of creating the whole list in memory at once.

- It pauses, remembers its state, and resumes from where it left off.

- If you think generators are “just fancy functions” — that’s wrong. They behave very differently.

-> Normal function vs Generator (core difference)

# ---Normal function---             ---Generator---

Runs fully                          Runs step-by-step

Returns once                        Uses yield instead of return

Loses all state                    Remembers where it stopped

"""