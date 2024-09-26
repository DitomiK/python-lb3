from transtation import g_trans

input_text = "Це лабораторна робота 3"

print(g_trans.TransLate(input_text, "auto", "pl"))
print(g_trans.LangDetect(input_text))
print(g_trans.CodeLang("pl"))
print(g_trans.CodeLang("Polish"))
print(g_trans.LanguageList("screen", "Добрий день"))
print(g_trans.LanguageList("file", "Добрий день"))
