import csv
import re
from itertools import groupby
from pprint import pprint

if __name__ == '__main__':

    with open("phonebook_raw.csv", encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # 1. Выполните пункты 1-3 задания.

    def fix_names_and_number(contacts: list)->list:

        pattern = r"(\+7|8)\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(?([доб.]*)?\s*(\d+)*\)?"
        pattern_repl = r'+7(\2)\3-\4-\5 \6\7'

        contacts_ = []

        for i, item in enumerate(contacts):
            fio = " ".join(item[:3]).split()

            while len(fio)<3:
                fio += ['']

            contacts_.append(fio + item[3:7])
            contacts_[i][5] = re.sub(pattern, pattern_repl, item[5]).strip()
        return contacts_
    
    def merging_duplicates(contacts: list)->list:
        contacts.sort(key=lambda x: (x[0], x[1]))
        res = []

        grouped_list = [list(data) for _, data in groupby(contacts, key=lambda x: (x[0], x[1]))]

        for list_ in grouped_list:            
            
            if len(list_)>1:
                while len(list_) != 1:
                    _ = []
                    for i, j in zip(list_[0], list_[1]):
                        if i==j:
                            _.append(i)
                        else:
                            _.append(i+j)

                    res.append(_)
                    list_.pop(1)
            else:
                res.append(list_[0])
        return res

    contacts = fix_names_and_number(contacts_list)

    contacts = merging_duplicates(contacts)

    pprint(contacts)

    # 2. Сохраните получившиеся данные в другой файл.
    # Код для записи файла в формате CSV:
    with open("phonebook.csv", "w" , encoding='utf8',newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts)

