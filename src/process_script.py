import os
import json
import re


def format_time(number, added=0):
    millis = number * 1000 + added
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(int(millis/(1000*60)))%60
    minutes = int(minutes)
    hours=(int(millis/(1000*60*60)))%24

    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{millis%1000:03d}'


def format_rst(json_file):
    out_file = json_file.replace(".json", '_f.srt')

    with open(json_file, 'r') as f:
        words = json.load(f)['words']

    f = open(out_file, 'w')
    i = 1
    for word in words:
        if word['case'] != "success":
            continue
        s = format_time(word['start'], -100)
        e = format_time(word['end'], 100)
        f.write(f'{i}\n')
        f.write(f"{s} --> {e}\n")
        f.write(f"{word['word']}\n\n")

        # print(i)
        # print()
        # print(word['word'])
        # print('\n')
        i+=1
    
    f.close()

def get_text(file_path):
    out_file = file_path.split('.')[0] + '.txt'
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    lines = [e for e in lines if re.fullmatch("(\w+\s*[,$-]*)+", e.strip())]
    lines2 = []

    for line in lines:
        if line not in lines2:
            lines2.append(line)

    with open(out_file, 'w') as f:
        f.writelines(lines2)

if __name__ == '__main__':
    # get_text('Phát âm chuẩn - Anh ngữ đặc biệt - Saving Money (VOA)-Dfo-7GOtEY8.en.vtt')
    format_rst('datasets/Phát âm chuẩn - Anh ngữ đặc biệt - Saving Money (VOA)-Dfo-7GOtEY8.json')