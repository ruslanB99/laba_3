# TODO  Напишите функцию count_letters
def count_letters(main_str):
    letters = {}
    lowercase_main_str= main_str.lower()
    for char in lowercase_main_str:
        if char.isalpha() and char.islower():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters
# TODO Напишите функцию calculate_frequency
def calculate_frequency(main_str):
    total_count = sum(main_str.values())
    frequencies = {}
    for main_str, count in main_str.items():
        frequency =format(count / total_count, ".2f")
        frequencies[main_str] = frequency
    return frequencies

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letters = count_letters(main_str)
frequencies = calculate_frequency(letters)
for letter, freq in frequencies.items():
    print(f"{letter}: {freq}")