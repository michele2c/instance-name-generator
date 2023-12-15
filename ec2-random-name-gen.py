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
# 4. Push your code to GitHub and include the link in your LinkedIn write up.

# example of format from AWS -> name-e7b1682894434ec5890312c7c403c011

import random
import string


num_instances = int(input("Number of instances: "))
dep_name = str.lower((input("Department name: ")))

# validate department name
if dep_name == "marketing" or dep_name == "accounting" or dep_name == "finops":
  # initialize list
    instances_list = []
    for i in range(num_instances):
      # define the lenght of the string
      str_size = 15
      # random part of the instance name
      random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=str_size))
      # combine department and random name
      instance_name = dep_name + "-" + random_name
      # append names to the list
      instances_list.append(instance_name)
    print(instances_list)
else:
    print("Sorry! Your department cannot use this tool.")
