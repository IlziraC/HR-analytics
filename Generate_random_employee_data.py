import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

manager_counter = 0
manager_ids = {}

def generate_random_employee(existing_managers):
    global manager_counter
    full_name = fake.name()
    employee_id = random.randint(100000, 999999)
    department = fake.random_element(elements=('Accounting', 'Marketing', 'HR', 'IT', 'Production', 'Sales', 'Logistics', 'Tech', 'Legal', 'Business Management'))
    position = fake.job()
    employee_type = fake.random_element(elements=('Full-time', 'Part-time', 'Contractor'))
    employee_type2 = fake.random_element(elements=('Permanent', 'Temporary'))
    separation_reason = fake.random_element(elements=('Voluntary', 'Involuntary'))
    gender = fake.random_element(elements=('Female', 'Male'))
    ethnicity = fake.random_element(elements=('Group A', 'Group B', 'Group c', 'Group D', 'Group E'))
    age = random.randint(21, 67)
    termination_date = (datetime.today - timedelta(days=random.randint(365, 365*5))).strftime('%Y-%m-%d')
    region = fake.random_element(elements=('North', 'Midwest', 'South', 'Central', 'Northwest', 'East'))    

    if employee_type == 'Full-time':
        working_hours = 40
    elif employee_type == 'Part-time':
        working_hours = random.choice([24, 32])
    else:
        working_hours = random.choice([24, 32, 40])

    hourly_rate = random.uniform(21, 90)
    employment_start_date = (datetime.now() - timedelta(days=random.randint(365, 365*6))).strftime('%Y-%m-%d')

    # Ensure 50 unique reporting_to values
    reporting_to = fake.random_element(elements=existing_managers)

    if reporting_to not in manager_ids:
        manager_counter += 1
        manager_ids[reporting_to] = str(manager_counter).zfill(6)

    reporting_to_id = manager_ids[reporting_to]

    return [full_name, employee_id, department, position, employee_type, employee_type2, working_hours, hourly_rate, employment_start_date, reporting_to, reporting_to_id, separation_reason,
            gender, ethnicity, age, termination_date, region]

# Generate 2000 random employees
existing_managers = ['Manager {}'.format(i) for i in range(1, 51)]
random_data = [generate_random_employee(existing_managers) for _ in range(3000)]

# Write to CSV file
csv_file_path = 'random_employee_data.csv'
header = ['Full name', 'Unique Employee ID', 'Department', 'Position', 'Employee Type', 'Employee Type 2', 'Working hours', 'Hourly rate', 'Employment start date', 'Reporting to', 'Reporting to ID',
          'Separation Reason', 'Gender', 'Ethnicity', 'Age', 'Termination Date', 'Region']

with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)
    csv_writer.writerows(random_data)

print(f"Random data has been generated and saved to {csv_file_path}")
