from file_to_flatdict import convert_to_flatdict as ctf
x = input("Please enter .yaml file as input:")
print(ctf.to_flatdict(x))
# print(ctf.to_flatdict("D:\Aishwarya_Work\Examples_Project\configs\conf2.yml"))