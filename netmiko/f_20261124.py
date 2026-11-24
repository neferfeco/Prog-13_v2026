from netmiko import ConnectHandler

csatlakozasi_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.254",
    "username": "pillerf",
    "password": "sshJelszo159"
}

try:
    with ConnectHandler(**csatlakozasi_adatok) as kapcsolat:
        # 1. feladat
        output_lista = kapcsolat.send_command("show ip interface brief | include down").strip().split('\n')
        #print(output_lista)
        
        '''for sor in output_lista:
            ind = sor.index(' ')
            if_azon = sor[0:ind]
            print(if_azon)'''

        for sor in output_lista:
            print(sor.split(' ')[0])




except Exception as ex:
    print(f"Hiba a csatlakozáskor: {ex}")




