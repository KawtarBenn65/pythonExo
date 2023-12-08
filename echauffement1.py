#produce_default_dict():
def produce_default_dict():
    default_dict = {'root': 'password'}
    return default_dict
print(produce_default_direct())

#fonction salutation
def salutation(nom, age):
    if age == '0':
        annee = 'an'
    else:
        annee = 'ans'
    message = f"Bonjour '{nom}', vous avez actuellement {age} {annee}."
    return message
print(salutation('gael', '12'))
print(salutation('bébé', '0'))

#def power_2
def power_2(limit):
    print(f"Nombres pairs jusqu'à {limit} : ", end="")
    for i in range(0, limit + 1, 2):
        print(i, end=" ")
    print()
power_2(10) 
#check_ip_format
def check_ip_format(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True
check_ip_format('192.12.')
  



  
