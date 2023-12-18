import os

current_path = os.path.dirname(os.path.abspath(__file__))
output_file_name = 'iptv.m3u'

files = [f for f in os.listdir(current_path) if os.path.isfile(os.path.join(current_path, f)) and f != output_file_name and f.endswith('.m3u')]

# Имя входного файла
input_file_name = files[0]

output_file_name = os.path.join(current_path, output_file_name)

# Открываем входной файл для чтения
with open(input_file_name, 'r', encoding='utf-8') as input_file:
    # Читаем все строки файла
    lines = input_file.readlines()

# Открываем выходной файл для записи
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    # Переписываем строки, содержащие слово "СССР"
    for idx, line in enumerate(lines):

        # EXTINF:0,BCU Action HD
        # EXTGRP:RU Кинозал
        #https: // as01.spr24.net / 20810 / mpegts?token = TnNy78ws9ANN32

        try:
            if any(i in lines[idx - 1].lower() for i in ['ссср', 'ussr']):
                line = '#EXTGRP:Советское кино\n'
                print(idx, line)
                print(idx + 2, lines[idx + 2])

            elif any(i in lines[idx - 1].lower() for i in ['comedy', 'комеди']):
                line = '#EXTGRP:Комедии\n'

            elif any(i in lines[idx - 1].lower() for i in ['marvel']):
                line = '#EXTGRP:Комедии\n'


            output_file.write(line)

        except:
            continue

print(f'Изменения сохранены в файле: {output_file_name}')