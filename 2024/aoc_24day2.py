from aocd import get_data
import pandas as pd
from io import StringIO

data = get_data(day=2, year=2024)

# Split the data into rows and columns manually
rows = [line.split() for line in data.split("\n") if line.strip()]

# Create a DataFrame from the list of rows
df = pd.DataFrame(rows)
df = df.apply(pd.to_numeric, errors='coerce')

def check_row_day2(inp):
    a = inp
# Initialise lists
    inc = []
    dec = []
    res = "Safe"
# Check whether the lists are strictly increasing/decreasing:
# If not, they are not safe:
    for c in range(len(a)-1):
        if a[c+1] > a[c]:
            inc.append(True)
        else:
            inc.append(False)
    for c in range(len(a)-1):
        if a[c+1] < a[c]:
            dec.append(True)
        else:
            dec.append(False)
# If the list is strictly increasing/decreasing,
# check if it increases/decreases by at most 3:
# If they do not satisfy this, they are not safe
    if all(inc):
        for c in range(len(a)-1):
            if a[c+1] - a[c] < 4:
                pass
            else:
                res = "Unsafe"
    elif all(dec):
        for c in range(len(a)-1):
            if a[c] - a[c+1] < 4:
                pass
            else:
                res = "Unsafe"
    else:
        res = "Unsafe"
# Return whether the list is safe or not
    return(res)

check_safe = []

for r in range(1000):
    a = df.iloc[r].dropna()
    s = check_row_day2(a)
    check_safe.append(s)

ans = check_safe.count("Safe")
ans = str(ans)

print("The number of safe lists is:")
print(ans)

# Part 2: Allow for one mistake
# We can do this by iteratively removing one and one item from the unsafe lists
# and check if they satisfy the conditions

def check_row_day2_with_one_mistake(inp):
    # First, check if the original sequence is safe
    a = inp.reset_index(drop=True)  # Reset index to match position indices
    if check_row_day2(a) == "Safe":
        return "Safe"
    
    # Iterate through each element in the sequence
    for i in range(len(a)):
        # Create a new sequence with the i-th element removed
        modified_sequence = a.drop(index=i).reset_index(drop=True)
        
        # Check if the modified sequence is safe
        if check_row_day2(modified_sequence) == "Safe":
            return "Safe"
    
    # If no modified sequence is safe, return "Unsafe"
    return "Unsafe"

check_safe_one_mistake = []
for r in range(1000):
    b = df.iloc[r].dropna()
    sm = check_row_day2_with_one_mistake(b)
    check_safe_one_mistake.append(sm)

ans2 = check_safe_one_mistake.count("Safe")
ans2 = str(ans2)

print("The number of safe lists, where one mistake is allowed, is:")
print(ans2)