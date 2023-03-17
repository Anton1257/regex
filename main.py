from pprint import pprint
import csv
import re


def read_phonebook() -> list:
    with open("phonebook_raw.csv") as f:
        return list(csv.reader(f, delimiter=","))

## 1. Выполните пункты 1-3 задания.
## Ваш код


def get_contacts(contacts_list: list) -> list:
    regex = re.compile(r'(\+7|8)\s*\(?(\d{3})\)?(\s*|-)(\d{3})(\s*|-*)(\d{2})-?(\d{2})(\s*(\(?(\доб.)?)\s*(\d{4}))?(\))*')
    contacts = dict()
    for is_not_title, row in enumerate(contacts_list):
        if is_not_title:
            firstname, lastname, surname = ','.join(row).replace(' ', ',').split(',')[:3]
            _ = {'firstname': firstname,
                 'lastname': lastname,
                 'surname': surname,
                 'organization': row[3],
                 'position': row[4],
                 'phone': regex.sub(r'+7(\2)\4-\6-\7 \10\11', row[5]),
                 'email': row[6]}
            if firstname not in contacts:
                contacts[firstname] = _
            else:
                for field in contacts[firstname]:
                    the_field_is_empty = not contacts[firstname][field]
                    if the_field_is_empty:
                        contacts[firstname][field] = _[field]
    return contacts


def write_phonebook(contacts: dict):
    ## 2. Сохраните получившиеся данные в другой файл.
    ## Код для записи файла в формате CSV:
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        ## Вместо contacts_list подставьте свой список:
        for contact in contacts.values():
            datawriter.writerow(contact.values())


if __name__ == '__main__':
    # чтение файла с контактами
    contacts_list = read_phonebook()
    # получение исправленного списка контактов
    contacts = get_contacts(contacts_list)
    # вывод списка в консоль
    pprint(contacts)
    # запись исправленного списка контактов в файл
    write_phonebook(contacts)
