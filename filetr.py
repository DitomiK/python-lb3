from transtation import g_trans, d_trans
from typing import Tuple
import re
import os

def text_statistics(text: str) -> Tuple[int, int, int]:
    num_characters = len(text)
    num_words = len(re.findall(r'\b\w+\b', text))
    num_sentences = len(re.findall(r'[.!?]', text))
    return num_characters, num_words, num_sentences

def read_config(config_file: str) -> Tuple[str, str, str, int, int, int]:
    try:
        with open(config_file, 'r') as file:
            lines = file.readlines()
            input_file = lines[0].strip()
            target_language = lines[1].strip()
            output_type = lines[2].strip()
            max_characters = int(lines[3].strip())
            max_words = int(lines[4].strip())
            max_sentences = int(lines[5].strip())
        return input_file, target_language, output_type, max_characters, max_words, max_sentences
    except Exception as e:
        raise Exception(f"Помилка при читанні конфігураційного файлу: {str(e)}")

config_file = 'config.txt'

try:
    input_file, target_language, output_type, max_characters, max_words, max_sentences = read_config(config_file)
except Exception as e:
    print(str(e))

if not os.path.isfile(input_file):
    print("Файл з текстом не знайдено.")

try:
    with open(input_file, 'r', encoding='utf-8') as file:
        text = ""
        while True:
            line = file.readline()
            if not line:
                break
            text += line
            num_characters, num_words, num_sentences = text_statistics(text)
            if num_characters > max_characters or num_words > max_words or num_sentences > max_sentences:
                break

    print(f"Назва файлу: {input_file}")
    print(f"Розмір файлу: {os.path.getsize(input_file)} байт")
    print(f"Кількість символів: {num_characters}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість речень: {num_sentences}")
    detected_language = g_trans.LangDetect(text, "lang")
    print(f"Мова тексту: {detected_language}")

    translated_text = d_trans.TransLate(text, detected_language, target_language)

    if output_type == "screen":
        print(f"Перекладений текст на {target_language}:")
        print(translated_text)
    elif output_type == "file":
        output_file = f"{os.path.splitext(input_file)[0]}_{target_language}.txt"
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print("Ok")
        except Exception as e:
            print(f"Помилка при запису в файл: {str(e)}")
    else:
        print("Помилка: Невірний тип виводу в конфігураційному файлі.")

except Exception as e:
    print(f"Помилка: {str(e)}")

