def replace_line(file_name, line_nim, text):
    lines = open(file_name, 'r', encoding = 'utf-8').readlines()
    lines[line_nim] = text
    out = open (file_name, 'w', encoding = 'utf-8')
    out.writelines(lines)
    out.close()

replace_line("test", 1, 'Hello')    