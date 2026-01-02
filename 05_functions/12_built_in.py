def chai_flavor(flavor="masala"):
    """Return the flavour of chai."""
    chai="ginger"
    return flavor

#That (__doc__) underscore underscore speak as "dunder" 

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

# help(len)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cupd (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    : return: (total amount, than you message)
    """
    total = chai*10 + samosa * 15
    return total, "Thank you for visiting chaicode.com"