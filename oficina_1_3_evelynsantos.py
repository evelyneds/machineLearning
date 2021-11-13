
#rodar no python --no Google Collab não roda o locale

from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,'pt_BR')



aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10', '12 Julho 1989', '16 de Junho de 1987', '04/07/1990']

patterns = ['%d/%m/%Y', '%d de %B de %Y', '%d/%b/%Y', '%Y-%B-%d', '%d %B %Y', '%d de %B de %Y']
birthdayList= []

for date in aniversarios:
    for pattern in patterns:
        try:
            birthdayList.append(datetime.strptime(date, pattern))
            break
        except:
            pass

birthdayToday = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

birthdayList.append(birthdayToday) #Incluido para testes

birthdayList= sorted(birthdayList, key = lambda d: (d.month, d.day))


for i in birthdayList:
    print(i.strftime('%d de %B de %Y'))


if birthdayToday in birthdayList:
    print(f"\õ/ Hoje, {birthdayToday.strftime('%a')} {birthdayToday.strftime('%d')} de {birthdayToday.strftime('%B')} de {birthdayToday.strftime('%Y')} tem aniversário! \õ/")
