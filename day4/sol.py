import re

f = open("test.txt", "r")
p = f.read()
f.close()

p = p.split("\n\n")

count = 0

for i in range(len(p)):
    a = {}
    x = p[i].split()
    for y in x:
        z = y.split(":")
        a[z[0]] = z[1]
    if "byr" in a and "iyr" in a and "eyr" in a and "hgt" in a and "hcl" in a and "ecl" in a and "pid" in a:
        if 1920 <= int(a["byr"]) <= 2002 and 2010 <= int(a["iyr"]) <= 2020 and 2020 <= int(a["eyr"]) <= 2030 and (("cm" in a["hgt"] and 150 <= int(a["hgt"][:-2]) <= 193) or ("in" in a["hgt"] and 59 <= int(a["hgt"][:-2]) <= 76)) and re.search(re.compile("^#[A-Fa-f0-9]{6}$"), a["hcl"]) and a["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and len(a["pid"]) == 9 and int(a["pid"]) >= 0:
            count += 1

print(count)