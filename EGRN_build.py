import xml.etree.ElementTree as ET
import os

# функция возвращает список .xml файлов из папки, включая подпапки, кроме proto_.xml
def get_file_list(path_Data):
    filelist = []
    for root, dirs, files in os.walk(path_Data):
        for file in files:
            if file.endswith(".xml") and file != "proto_.xml":
                filelist.append(os.path.join(root, file))
    return filelist


#  MIF Функция парсит ЕГРН и вытаскивает правообладателей
def make_list_right_holders(file_name):
    list_right_holders = []
    tree = ET.parse(file_name)
    build_records = tree.findall('build_record/object/common_data')
    for build_record in build_records:
        cad_number = build_record.find('cad_number').text
        list_right_holders.append(cad_number)
    # ------------------------------возвращает список правообладателей----------------------------------------------
    right_holders = tree.findall('right_records/right_record/right_holders/right_holder/individual')
    for right_holder in right_holders:
        #  ---------------------------возвращает ФИО правообладателя----------------------------
        surname = right_holder.find('surname').text
        name = right_holder.find('name').text
        patronymic = right_holder.find('patronymic').text
        list_right_holders.append(surname)
        list_right_holders.append(name)
        list_right_holders.append(patronymic)

    return list_right_holders

if __name__ == '__main__':
    path_file_rezult = str(input('Укажите путь к папке, куда сохранить данные в формате D:/project_Python/XML_Parser/1 '))
    path_Data = str(input('Укажите путь к папке, где содержатся ЕГРН на ОКС в формате D:/project_Python/XML_Parser/1 '))

    # -------------------------Открываем поочередно кпт.xml файлы----------------------------------
    filelist = get_file_list(path_Data)
    for file_name in filelist:
        print(make_list_right_holders(file_name))
        file_rezult = open(path_file_rezult + '/rezult.txt', 'a')
 # ------------------------записываем полученный список в mif файл-------------------------------
        list_right_holders = make_list_right_holders(file_name)
        file_rezult.write(str(list_right_holders) + '\n')
        file_rezult.close()


