from netmiko import ConnectHandler

csatlakozasi_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.254",
    "username": "pillerf",
    "password": "sshJelszo159"
}


try:
    with ConnectHandler(**csatlakozasi_adatok) as kapcsolat:
        # print(kapcsolat.find_prompt())
        
        # print(kapcsolat.check_enable_mode())
        
        # print(kapcsolat.save_config())
        
        #output = kapcsolat.send_command("show running-config")
        #print(output)


        # Mi az eszköz neve?
        # A1)
        output = kapcsolat.find_prompt()
        
        output = output.rstrip('#')
        #print(output)
        
        # A2)
        #print(output[0:-1])
        
        
        # B)
        output = kapcsolat.send_command("show running-config").split('\n')
        #print(output)
        
        i = 0
        while 'hostname' not in output[i]:
            i += 1

        #print(output[i].split(' ')[1])


        # C)
        output = kapcsolat.send_command("show running-config | include hostname").strip()
        #print(output[i].split(' ')[1])
        
        
        ###
        # VLAN-ok száma?
        ###
        output = kapcsolat.send_command('show vlan summary | include existing VLANs')
        
        print(f"VLAN-ok száma a kapcsolón: {output.strip().split(':')[1].strip()}")
        


except Exception as ex:
    print(f"Hiba a csatlakozáskor: {ex}")




