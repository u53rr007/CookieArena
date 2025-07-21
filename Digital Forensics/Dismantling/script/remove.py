with open('dns.txt', 'r') as f:
    lines = f.readlines()

data = [line.split('.')[0] +"\n" for line in lines]

with open('dns_cleaned.txt', 'w') as f:
    f.writelines(data)
