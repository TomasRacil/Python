import re

text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

print(
    sum(
        [int(pair[0]) * int(pair[1]) for pair in re.findall("mul\((\d+),(\d+)\)", text)]
    )
)

print(re.findall("(don't\(\))|(do\(\))|mul\((\d+),(\d+)\)", text))
