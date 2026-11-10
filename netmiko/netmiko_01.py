from netmiko import ConnectHandler

csatlakozasi_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.254",
    "username": "pillerf",
    "password": "Jelszo123"
}


try:
    with ConnectHandler(**csatlakozasi_adatok) as kapcsolat:
        print(kapcsolat.find_prompt())

except Exception as ex:
    print(f"Hiba a csatlakozáskor: {ex}")




