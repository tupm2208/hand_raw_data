import os

f = open('Phát âm chuẩn - Anh ngữ đặc biệt - Saving Money (VOA)-Dfo-7GOtEY8.en.vtt', 'r')

lines = [e for e in f.readlines() if "position:0%" not in e and "><" not in e and ' \n' != e and '\n' != e]
# out = list(set(lines))
out = {}

for e in lines:
    out[e] = 1

out = list(out.keys())[3:]

with open('out_text.txt', 'w') as f:
    f.writelines(out)