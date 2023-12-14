"""
Project - EC2 Random Name Generator
"""
# **Use Case**

# Several departments share an AWS environment. You need to 
# ensure that the EC2s are properly named and are unique so team members 
# can easily tell who the EC2 instances belong to. Use Python to create 
# your unique EC2 names that the users can then attach to the instances. 

# The Python Script should:

# 1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
# 2. Allow the user to input the name of their department that is used in the unique name.
# 3. Generate random characters and numbers that will be included in the unique name.

# 4. The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. 
# List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. 
# Be sure to account for incorrect upper or lowercase letters in the correct department. Example: a user inputs accounting vs Accounting.

# 5. Turn the above into a Function and execute the Function to verify it works.

# example of format from AWS -> name-e7b1682894434ec5890312c7c403c011

import random
import string


num_instances = int(input("Number of instances: "))
dep_name = str(input("Department name: "))

# validate department name
if dep_name.lower() == "marketing" or dep_name.lower() == "accounting" or dep_name.lower() == "finops":
  # initialize list
    instances_list = []
    for x in range(num_instances):
      x += 1
      # define the lenght of the string
      str_size = 15
      # random part of the instance name
      random_name = ''.join(random.choices(string.hexdigits, k=str_size))
      # combine department and random name
      instance_name = dep_name.lower() + "-" + random_name.lower()
      # append names to the list
      instances_list.append(instance_name)
    print(instances_list)
else:
    print("Sorry! Your department cannot use this tool.")
