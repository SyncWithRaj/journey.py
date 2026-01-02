# def make_chai():
    # return "Here is your masala chai"
    # print("Here is your masala chai")

# return_value = make_chai()

# print(return_value)


def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai Over"
    return "Chai is ready"
    print("chai")

print(chai_status(0))
print(chai_status(5))



def chai_report():
    return 100, 20, 10  # sold, remaining

sold, remaining, not_paid = chai_report()

print("Sold: ", sold)
print("Remaining: ", remaining)

#if you return more value than the variables there use under score to ignore more values:
# eg: def chai_report():
#     return 100, 20, 10, 45, 56  # sold, remaining

# sold, remaining, _ = chai_report()  # That underscore cause printing of only first two values for sold, and remaining