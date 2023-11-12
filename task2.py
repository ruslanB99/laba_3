# TODO Напишите функцию find_common_participants
def find_common_participants(str1,str2,i=','):
    participants_first_group=str1.split(i)
    participants_second_group=str2.split(i)
    common_participants=list(set(participants_first_group) & set(participants_second_group))
    common_participants.sort()

    return common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
