# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants( participants_first_group, participants_second_group, sep=','):
    group1 = participants_first_group.split(sep)
    group2 = participants_second_group.split(sep)
    common_participants_list = []
    for participants in group1:
        if participants in group2:
            common_participants_list.append(participants)
            common_participants_list.sort()
    return common_participants_list


# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, sep='|'))