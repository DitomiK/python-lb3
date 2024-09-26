from deep_translator import GoogleTranslator
from langdetect import detect



def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        language = detect(text)
        if set == "lang":
            return language
        else:
            return f"Мова: {language}"
    except Exception as e:
        return f"Error: {str(e)}"


def CodeLang(lang: str) -> str:
    try:
        supported_languages = GoogleTranslator().get_supported_languages(as_dict=True)
        lang = lang.lower()
        if lang in supported_languages.values():
            for code, name in supported_languages.items():
                if name == lang:
                    return code
        elif lang in supported_languages:
            return supported_languages[lang]
        else:
            return "Помилка: Неправильна мова або код мови."
    except Exception as e:
        return f"Error: {str(e)}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        supported_languages = GoogleTranslator().get_supported_languages(as_dict=True)
        result = []
        header = f"{'N':<4} {'Language':<20} {'ISO-639 code':<15}"

        if text:
            header += "Text"
        result.append(header)
        result.append('-' * 60)

        for idx, (code, lang) in enumerate(supported_languages.items(), 1):
            line = f"{idx:<4} {lang:<20} {code:<15}"
            if text:
                translated_text = GoogleTranslator(target=code).translate(text)
                line += translated_text
            result.append(line)

        output = '\n'.join(result)

        if out == "file":
            with open('languages_deeptr.txt', 'w', encoding='utf-8') as file:
                file.write(output)
            return "Ok"
        else:
            print(output)
            return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
