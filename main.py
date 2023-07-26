from pprint import pprint
import csv
import re
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  
# print(contacts_list)

# [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'], ['Усольцев Олег Валентинович', '', '', 'ФНС', 'главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц', '+7 (495) 913-04-78', 'opendata@nalog.ru'], ['Мартиняхин Виталий Геннадьевич', '', '', 'ФНС', '', '+74959130037', ''], ['Наркаев', 'Вячеслав Рифхатович', '', 'ФНС', '', '8 495-913-0168', ''], ['Мартиняхин', 'Виталий', 'Геннадьевич', 'ФНС', 'cоветник отдела Интернет проектов Управления информационных технологий', '', '', ''], ['Лукина Ольга Владимировна', '', '', 'Минфин', '', '+7 (495) 983-36-99 доб. 2926', 'Olga.Lukina@minfin.ru'], ['Паньшин Алексей Владимирович', '', '', 'Минфин', '', '8(495)748-49-73', '1248@minfin.ru'], ['Лагунцов Иван Алексеевич', '', '', 'Минфин', '', '+7 (495) 913-11-11 (доб. 0792)', ''], ['Лагунцов Иван', '', '', '', '', '', 'Ivan.Laguntcov@minfin.ru']]

for person in contacts_list:
  per_0 = person[0]
  per_1 = person[1]
  per_2 = person[2]
  per_0_list = per_0.split()
  per_1_list = per_1.split()
  per_2_list = per_2.split()
  if len(per_0_list) == 3:
    person[0] = per_0_list[0]
    person[1] = per_0_list[1]
    person[2] = per_0_list[2]
  if len(per_0_list) == 2:
    person[0] = per_0_list[0]
    person[1] = per_0_list[1]
  if len(per_1_list) == 3:
    person[0] = per_0_list[0]
    person[1] = per_0_list[1]
    person[2] = per_0_list[2]
  if len(per_1_list) == 2:
    person[1] = per_1_list[0]
    person[2] = per_1_list[1]
  if len(per_2_list) == 3:
    person[0] = per_2_list[0]
    person[1] = per_2_list[1]
    person[2] = per_2_list[2]
  if len(per_2_list) == 2:
    person[1] = per_2_list[0]
    person[2] = per_2_list[1]

  
# print(contacts_list)

pattern =r"(\+7|8)\s*\(?(495)\)?[\s-]*(\d{3})[-]*(\d{2})[\s-]*(\d+)\s*\(?(доб.)?\s?(\d+)?\)?"
sub_ = r" +7(\2)\3-\4-\5 \6\7 "
contacts_list_newphones = []
for cont in contacts_list:
  cont_list=[]
  for el in cont:
    result = re.sub(pattern, sub_, el)
    cont_list.append(result)
  contacts_list_newphones.append(cont_list)




for a in range(len(contacts_list_newphones)):
  for b in range(a+1, len(contacts_list_newphones)):
    for c in range(len(contacts_list_newphones[0])):
      if contacts_list_newphones[a][0] == contacts_list_newphones[b][0] and contacts_list_newphones[a][1] == contacts_list_newphones[b][1] and contacts_list_newphones[a][c] == '':
        contacts_list_newphones[a][c] += contacts_list_newphones[b][c]




fam_name_list=[]


final_contacts_list = []

for el in contacts_list_newphones:
    famname = " ".join(el[:2])
    if famname not in fam_name_list :
        fam_name_list.append(famname)
        final_contacts_list.append(el)
# print(final_contacts_list)

# Записываем финишный список списков в CSV-файл 'phonebook_2.csv'
with open('phonebook_2.csv', 'w',encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(final_contacts_list)