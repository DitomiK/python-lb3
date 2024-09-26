from transtation import d_trans

input_text = "Це лабораторна робота 3"

print(d_trans.TransLate(input_text, "auto", "pl"))
print(d_trans.LangDetect(input_text))
print(d_trans.CodeLang("pl"))
print(d_trans.CodeLang("Polish"))
print(d_trans.LanguageList("screen", "Добрий день"))
print(d_trans.LanguageList("file", "Добрий день"))