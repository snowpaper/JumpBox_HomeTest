group = {
    'A': 20,
    'B': 15,
    'C': 10
}
"""
group = {
    'A': 10,
    'B': 30,
    'C': 105
}
"""
# Method to split the bill
def split_the_bill(x):
    total_each_owed = sum(x.values())/float(len(x))
    return {key:round(value - total_each_owed, 5) for key, value in x.items()}

# Input group
if __name__ == "__main__":
	print(split_the_bill(group))
