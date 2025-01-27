import re

with open('1.csv', 'r', encoding='utf-8') as file1, open('2.csv', 'r', encoding='utf-8') as file2:
    text1 = file1.read()
    text2 = file2.read()

email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
emails1 = email_pattern.findall(text1)
emails2 = email_pattern.findall(text2)

all_emails = set(emails1 + emails2)

for email in all_emails:
    print(email)

print(f"\nTotal of {len(all_emails)} different email have been found.")
