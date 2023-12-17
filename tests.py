

# # use this example tp make a list for departments for the project
# dep_names = ['marketing', 'accounting', 'finops']
# dep_name = str.lower(input('Department: '))
# if dep_name not in dep_names:
#   print('Ooops... Your department cannot use this tool.')
# # else:
#call function

# import random
# import string

# # function random characteres
# def generate_instance_name(dep_name):
#   str_size = 15
#   random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=str_size))
#   # print(dep_name.lower() + "-" + random_name)
#   return dep_name.lower() + "-" + random_name

# # department validation name
# # with the IF stament
# # if correct return dep name
# # if wrong re assing dep name 
# def handle_department():
#   dep_name = str(input("Department name: "))
#   return dep_name

# # function number of instances and generate names
# def instance_generator_name():
#   num_instances = int(input("Number of instances: "))
#   dep_name = handle_department()
# # if dep name = not valid 
#   # print blah 
# # else: 
#   # do the for loop
#   if dep_name.lower() == "marketing" or dep_name.lower() == "accounting" or dep_name.lower() == "finops":
#     instances_list = []
#     for x in range(num_instances):
#       x +=1
#       instance_name = generate_instance_name(dep_name)
#       instances_list.append(instance_name)
#     print(instances_list)
#   else:
#     print("Sorry! Your department cannot use this tool.")

# instance_generator_name()
