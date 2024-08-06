def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100 

    if efficiency >= 80:
        print('Status: Green')
    elif efficiency >= 60:
        print('Status: Orange')
    elif efficiency >= 30:
        print('Status: Red')
    else:
        print('Status: Black')

def shutdown_machine():
   
    print('Shutting down the machine...')

def safety_protocol(temperature, neutrons_emitted):
    threshold = temperature * neutrons_emitted * 100
    threshold_percentage = (temperature * neutrons_emitted * 100) / threshold
    
    if threshold_percentage < 90:
        print('LOW LEVEL: control rods should be removed to produce energy.')
    elif 1 <= threshold_percentage < 10:
        print('The machine is in normal state.')
    else:
        print('DANGER......')
        print('Leave the area.')
        print('The safety protocol has been triggered....')
        shutdown_machine()  


machine_temperature = int(input('Temperature in K: '))
machine_neutrons_emitted = int(input('Number of neutrons emitted per second: '))
result = is_criticality_balanced(machine_temperature, machine_neutrons_emitted)

if result:
    print('The machine is in critical state.')
    

    safety_protocol(machine_temperature, machine_neutrons_emitted)
    

    voltage_user = int(input('What is the machine voltage?: '))
    current_user = int(input('What is the machine current?: '))
    max_power_user = int(input('What is the theoretical maximum power?: '))
    
    user_machine_efficiency = reactor_efficiency(voltage_user, current_user, max_power_user)
else:
    print('The machine is not in critical state.')

