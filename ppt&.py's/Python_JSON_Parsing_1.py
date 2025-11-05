# Python JSON Parsing Example - Print Employee Roles
# Python JSON Parsing Example - Print Employee Roles
# ---------------------------------------------------

import json

# JSON data (string)
json_data = '''
{
    "employees": [
        {"name": "Aisha", "role": "Manager"},
        {"name": "Rahul", "role": "Developer"},
        {"name": "Fatima", "role": "Data Analyst"}
    ]
}
'''

# Parse JSON string
data = json.loads(json_data)

# Loop through employees and print their details
print("Employee List:")
for emp in data.get("employees", []):
    try:
        print(f"Name: {emp['name']} | Role: {emp['role']}")
    except KeyError:
        print("⚠️ Missing data for one employee")

# Nested JSON example
nested_data = {
    "department": "IT",
    "employees": [
        {"name": "Ali", "skills": ["Python", "AWS"]},
        {"name": "Sara", "skills": ["SQL", "ETL"]}
    ]
}

print("\nNested Employee Skills:")
for emp in nested_data["employees"]:
    print(f"{emp['name']} skills: {', '.join(emp['skills'])}")

# Summary note
"""
- Use json.loads() for JSON strings
- Access keys safely with .get() or try/except
- Loop through lists to extract fields
- Ideal for processing JSON-based ETL data
"""
