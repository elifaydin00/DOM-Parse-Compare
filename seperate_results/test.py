import re

# Example input string
input_string = '</div><div class="glider-slide active center visible" data-gslide="1"'

# Define the regular expression pattern
pattern = r'glider-slide ([^"]+)'

# Find the match using the pattern
match = re.search(pattern, input_string)

# Extract the captured string
if match:
    captured_string = match.group(1)
    print(captured_string)