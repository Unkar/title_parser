import easygui

#Главное меню
def main_menu():
    msg = "Выберите действие"
    title = "Парсинг отчётов выноса"
    choices = ["Парсинг", "Просмотр логов", "Выход"]
    reply = easygui.buttonbox(msg, title, choices)
    return reply

#Парсинг
def parsing():
    file = easygui.fileopenbox(filetypes=["*.htm", "*.html"], multiple=True)
    return file

#Просмотр логов
def logs(logs):
    easygui.textbox(msg="Логи", title="Логи", text=logs)

#Сохранение файла
def save_file(data):
    file = easygui.filesavebox(filetypes=["*.csv", "*.xlsx"], default="*.csv")
    return file

#Сообщение об ошибке
def error(msg):
    easygui.msgbox(msg=msg, title="Ошибка", ok_button="OK")
