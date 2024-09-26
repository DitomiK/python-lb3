from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Мова: {detection.lang}, Точність: {detection.confidence}"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang):
    if lang in LANGUAGES:
        return LANGUAGES[lang]

    for code, name in LANGUAGES.items():
        if lang.lower() == name.lower():
            return code

    return "Мова не знайдена"


def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        result = []
        header = f"{'N':<4} {'Language':<20} {'ISO-639 code':<15}"

        if text:
            header += "Text"
        result.append(header)
        result.append('-' * 60)

        for idx, (code, lang) in enumerate(LANGUAGES.items(), 1):
            line = f"{idx:<4} {lang:<20} {code:<15}"
            if text:
                translated_text = translator.translate(text, dest=code).text
                line += translated_text
            result.append(line)

        output = '\n'.join(result)

        if out == "file":
            with open('../languages_gtrans.txt', 'w', encoding='utf-8') as file:
                file.write(output)
            return "Ok"
        else:
            print(output)
            return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"

