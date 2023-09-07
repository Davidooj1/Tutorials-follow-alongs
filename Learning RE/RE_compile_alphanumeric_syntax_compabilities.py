import re

emails = '''
CoreyMSchafer@gmail.com yoo
corey.schafer@university.edu
corey-321-schafer@my-work.net'''

pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")

matches = pattern.finditer(emails)

for match in matches:
    print(match)

print(matches)

match2 = re.search(r"[a-zA-Z]", emails)

# This was apart of a tutorial on freecodecamp when I was doing Scientific Computing with Python course.
