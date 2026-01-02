device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("Hight Temperature Alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")
