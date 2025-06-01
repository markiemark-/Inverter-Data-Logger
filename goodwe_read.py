import asyncio
import goodwe


async def get_runtime_data():
    ip_address = '192.168.2.225' 

    inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()

    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data:
            print(f"{sensor.id_} : \t\t {sensor.name} = {runtime_data[sensor.id_]} {sensor.unit}")
           # print(f"{runtime_data['pgrid1']}")
           # print(f"{runtime_data['e_total']}")


asyncio.run(get_runtime_data())

#timestamp :                Timestamp = 2025-06-01 14:11:25 
#vpv1 :                     PV1 Voltage = 199.7 V
#ipv1 :                     PV1 Current = 7.4 A
#ppv1 :                     PV1 Power = 1478 W
#vpv2 :                     PV2 Voltage = 0.0 V
#ipv2 :                     PV2 Current = 0.0 A
#ppv2 :                     PV2 Power = 0 W
#ppv :                      PV Power = 1478 W
#vline1 :                   On-grid L1-L2 Voltage = 0 V
#vgrid1 :                   On-grid L1 Voltage = 240.6 V
#igrid1 :                   On-grid L1 Current = 6.1 A
#fgrid1 :                   On-grid L1 Frequency = 50.0 Hz
#pgrid1 :                   On-grid L1 Power = 1468 W
#total_inverter_power :     Total Power = 1506 W
#work_mode :                Work Mode code = 1 
#work_mode_label :          Work Mode = Normal 
#error_codes :              Error Codes = 0 
#warning_code :             Warning code = 0 
#apparent_power :           Apparent Power = -1 VA
#reactive_power :           Reactive Power = -1 var
#power_factor :             Power Factor = -0.001 
#temperature :              Inverter Temperature = 41.0 C
#e_day :                    Today's PV Generation = 6.2 kWh
#e_total :                  Total PV Generation = 9698.1 kWh
#h_total :                  Hours Total = 17679 h
#safety_country :           Safety Country code = 20 
#safety_country_label :     Safety Country = NL-A 
#funbit :                   FunBit = 336 
#vbus :                     Bus Voltage = 379.8 V
#vnbus :                    NBus Voltage = 0 V
#derating_mode :            Derating Mode code = 0 
#derating_mode_label :      Derating Mode =  
#active_power :             Active Power = -1 W