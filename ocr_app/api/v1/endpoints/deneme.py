import re

text = """
Here are some example phone numbers:
05551234567
05071234567
05321234567
05411234567
0555 123 45 67
+905551234567
+90 555 123 45 67
0 (555) 123 45 67
"""

pattern = r'(?:(?:\+?90\s?)|0\s?)?(?:(\d{3})[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})|(\d{4})(\d{3})(\d{2})(\d{2}))'
matches = re.findall(pattern, text)

formatted_numbers = [' '.join(match) for match in matches]
print(formatted_numbers)