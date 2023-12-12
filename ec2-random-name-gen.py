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

# marketing-e7b1682894434ec5890312c7c403c011

import random
import string

department_name = str(input("Department: "))
number_instances = int(input("Number of instances: "))

# initialize an empty list
instances_list = []
# initialize while loop counter
counter = 1

while counter <= number_instances:
    # initializing size of string
    string_size = 32
    # use random.choices() to randomly choose characters and numbers
    # ''.join() to join the list of characters
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=string_size))
    # store department name in lowercase + random string
    instances = department_name.lower() + "-" + random_name
    # append result to the list
    instances_list.append(instances)
 
    counter += 1 #increment by 1


print(instances_list)

