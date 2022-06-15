
import numpy
import pandas as pd
import win32com.client as client


data = pd.read_excel('Входные данные.xlsx', sheet_name='Лист1')
logins = []
for login in data['login'].array:
    if not login in logins:
        logins.append(login)
    else:
        continue
servers = []
for server in data['servers'].array:
    if not server in servers:
        servers.append(server)
    else:
        continue
print(logins)
print(data.servers)

def sending(logins):
    outlook = client.Dispatch('Outlook.Application')
    for login in logins:
        message = outlook.CreateItem(0)
        message.Display(0)
        message.To = str(login) + '@gmail.com'
        message.Subject = 'Test'
        message.Body = str(data[data.login == login].iloc[:, 1])

    #message.Send()

sending(logins)