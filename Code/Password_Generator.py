import random
import PySimpleGUI as sg
import os


class PassGen:

    def __init__(self):
        #Layout
        list_email = ['gmail.com', 'hotmail.com', 'outlook.com', 'icloud.com', 'yahoo.com', '']

        sg.theme('LightBlue4')
        layout = [
            [sg.Text('Site/Software: ', size=(10, 1)),
            sg.Input(key='site', size=(45, 1))],
            [sg.Text('E-mail: ', size=(10, 1)),
            sg.Input(key='email', size=(25, 1)), sg.Text('@: ', size=(2, 1)), sg.Combo(list_email, key='list_email')],
            [sg.Text('User: ', size=(10, 1)),
            sg.Input(key='user', size=(45, 1))],
            [sg.Text('Password Format: ', size=(20, 1)), sg.Text('          Number of Characters:    '), sg.Combo(values=list(range(51)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Checkbox('Numbers', default=True, key='cb_numbers'), 
            sg.Checkbox('Capital letters', default=True, key='cb_cap_letters'), 
            sg.Checkbox('Small letters', default=True, key='cb_sml_letters'), 
            sg.Checkbox('Others', default=True, key='cb_others')],
            [sg.Output(size=(56, 5))],
            [sg.Button('Gen. Password')]
        ]

        self.janela = sg.Window('Password Generator', layout)


    def Start(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Gen. Password':
                new_pgen = self.Generate_Password(values)
                print(new_pgen)
                self.Save_Password(new_pgen, values)

    def Generate_Password(self, values):
        char_list = ''
        list1 = ''
        list2 = ''
        list3 = ''
        list4 = ''

        if values['cb_numbers'] == True:
            list1 = '1234567890'
        if values['cb_cap_letters'] == True:
            list2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if values['cb_sml_letters'] == True:
            list3 = 'abcdefghijklmnopqrstuvwxyz'
        if values['cb_others'] == True:
            list4 = '?!@#$%¨&*-_=+§}.,:><";{][)(/'
        
        char_list = list1 + list2 + list3 + list4
        chars = random.choices(char_list, k=int(values['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    
    def Save_Password(self, new_pgen, values):
        with open('Passwords.txt', 'a', newline='') as file:
            file.write(f"--> Site:  {values['site']}\nE-mail:    {values['email']}@{values['list_email']}\nUser:      {values['user']}\nPassword:  {new_pgen}")
            file.write(f"\n_______________________________________________________________________\n")

        print('Save File')



gen = PassGen()
gen.Start()
