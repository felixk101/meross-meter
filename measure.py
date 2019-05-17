from meross_iot.api import MerossHttpClient
from meross_iot.supported_devices.power_plugs import GenericPlug
from meross_iot.supported_devices.light_bulbs import GenericBulb
import secret

httpHandler = MerossHttpClient(email=secret.email, password=secret.password)
device = httpHandler.list_supported_devices()[0]

def turnOn():
    device.turn_on_channel(0)

def turnOff():
    device.turn_off_channel(0)

def getPowerConsumption():
    return device.get_power_consumption()

def getElectricityConsumption():
    return device.get_electricity()

if __name__=='__main__':

    httpHandler = MerossHttpClient(email="felixk101@gmail.com", password="fk412834")
    print("Listing online devices...")

    # Retrieves the list of supported and ONLINE devices.
    # If you also want to list offline devices, pass the online_only=False parameter.
    # Note! Trying to control an offline device will generate an exception.
    device = httpHandler.list_supported_devices()[0]
    print("\n-------------------------------\n"
          "Playing with device: %s"
          "\n-------------------------------" % device)

    # Returns most of the info about the power plug
    print("\nGetting system data...")
    data = device.get_sys_data()
    print(data)

    # Turns the power-plug off
    print("\nTurning power off")
    device.turn_off_channel(0)

    # Turns the power-plug on
    print("\nTuring power on")

    # Some devices support reading consumption data
    if device.supports_consumption_reading():
        print("\nReading consumption data...")
        consumption = device.get_power_consumption()
        print(consumption)

    # Some devices support reading consumption data
    if device.supports_electricity_reading():
        print("\nReading electricity data...")
        electricity = device.get_electricity()
        print(electricity)
