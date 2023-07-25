import csv
import re
from pprint import pprint

if __name__ == '__main__':

    with open("phonebook_raw.csv", encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        # pprint(contacts_list)


    
    for i, _ in enumerate(contacts_list):
        fio = " ".join(_[:3]).split()
        _list = fio+_[3:]
        pprint(_list)

        ## 1. Выполните пункты 1-3 задания.
        ## Ваш код

        ## 2. Сохраните получившиеся данные в другой файл.
        ## Код для записи файла в формате CSV:
        # with open("phonebook.csv", "w") as f:
        # datawriter = csv.writer(f, delimiter=',')
        
        # ## Вместо contacts_list подставьте свой список:
        # datawriter.writerows(contacts_list)