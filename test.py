import re , sys

str = " 2003\/2007/CD "
check = "2003\/2007/CD"
result = re.findall(r"\d+(?P<pattern>.*)\d+/\w+",str)
print(result)
if check == result:
    print(result)

