# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
new_record = ('Igor', 'Kovalchuk', 36, 'Engineer', 'Kostopil')
print("------Add new record to the begining", "\n", people_records)
print("length before insert 'new_record' - ", len(people_records), '\n')
people_records.insert(0, new_record)
print(people_records)
print("length after insert 'new_record' - ", len(people_records), '\n')

print("----Swap the elements with indexes 1 and 5", '\n', 'index 1', people_records[1], '\n', 'index 5', people_records[5], '\n')
people_records[1], people_records[5] = people_records[5], people_records[1]
print(' index 1', people_records[1], '\n', 'index 5', people_records[5], '\n')

print("----Check indexes [6] [10] [13] and age >= 30 ")
indexes_to_check = [6, 10, 13]
all_ages_gt_30 = True
for index in indexes_to_check:
  print('index-', index, " Age-", people_records[index][2])
  age = people_records[index][2]
  if age < 30:
    all_ages_gt_30 = False
print('All ages grater then 30 =', all_ages_gt_30)