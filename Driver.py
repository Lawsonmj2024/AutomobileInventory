'''
Portfolio Project
Michael Lawson
Colorado State University, Global
ITS320: Intro to Programming
Dr. Anwar Ahmed
January 15, 2023
'''

# Import Inventory and Automobile classes
from Main import InventoryClass
from Main import AutomobileClass

def add_vehicle(inventory):
    '''Controls input for adding a vehicle to inventory'''
    # Instantiates a new vehicle object
    vehicle = AutomobileClass.Automobile()
    
    # Captures VIN from user
    print('Enter the VIN to add a vehicle to inventory:')
    _update_attribute(vehicle.set_VIN, 'VIN')
    print()
    
    # Confirms VIN is not already in inventory
    if inventory.find_vehicle(vehicle.get_VIN()) == None:
        # Set the rest of the vehicle attributes
        print('Enter the following information about the vehicle:')
        choose_attribute(vehicle, 'Year')
        choose_attribute(vehicle, 'Make')
        choose_attribute(vehicle, 'Model')
        choose_attribute(vehicle, 'Color')
        choose_attribute(vehicle, 'Mileage')
        
        # Add vehicle to inventory
        inventory.add(vehicle)
        print('Vehicle was added to inventory.')
        print()
        
        # Display vehicle for confirmation
        display_automobile(vehicle)
    else:
        print('Vehicle already in inventory, returning to menu.')

def remove_vehicle(inventory):
    '''Controls inputs for removing a vehicle from inventory'''
    # Do nothing if the inventory is empty
    if inventory.is_empty():
        return
    
    # Display inventory for user to select vehicle to remove
    display_inventory(inventory)
    
    # Attempt to remove vehicle using VIN provided by user
    VIN = input('Enter the VIN of the vehicle to remove: ')
    vehicle = inventory.find_vehicle(VIN)
    if vehicle == None:
        print('VIN not found')
    elif inventory.remove(vehicle):
        print('Vehicle was removed from inventory.')

def update_vehicle(inventory):
    '''Controls inputs for updating a vehicle that is in inventory'''
    # Do nothing if inventory is empty
    if inventory.is_empty():
        return
    
    # Display inventory for user to select vehicle to update
    display_inventory(inventory)
    
    # Confirm VIN is in inventory
    VIN = input('Enter the VIN of the vehicle to update:\n')
    vehicle = inventory.find_vehicle(VIN)
    
    if vehicle == None:
        print('VIN not found')
    else:
        # Display selected vehicle to user
        display_automobile(vehicle)
        
        # User specifies attribute and enters new value
        att = input('Enter the attribute to update: ')
        choose_attribute(vehicle, att.capitalize())
        print()
        
        # Display updated vehicle data
        display_automobile(vehicle)

def save_inventory(inventory):
    if not inventory.is_empty():
        print('Would you like to save inventory to a file?')
        print('[y] Save inventory to file')
        print('[n] Exit without saving')
        print()
        save = input('Enter an option: ')
        print()
        if not save == 'n':
            print('Saving to file...', end='')
            inventory.save_to_file(_inventory_header() + '\n', 'inventory.txt')
            print('Complete')

def display_automobile(vehicle):
    '''Displays a single vehicle'''
    # Print header row for vehicle lists
    _display_inventory_header()
    
    # Print specified vehicle
    print(str(vehicle))
    print()
    
def display_inventory(inventory):
    '''Displays the inventory'''
    # Print header row for vehicle lists
    _display_inventory_header()
    
    # Print all vehicles in inventory
    inventory.display()
    print()

def _inventory_header():
    '''Return formatted string containing attribute names'''
    s = str('%-17s  %-4s %-20s %-10s %13s\n' % ('VIN', 'Yr', 'Make/model', 'Color', 'Mileage'))
    s += str('-'*69)
    return s

def _display_inventory_header():
    '''Print formatted String containing attribute names'''
    print(_inventory_header())

def choose_attribute(vehicle, attribute):
    '''Select the attribute to modify for the specified vehicle'''
    if attribute == 'Year' or attribute == 'Yr':
        _update_attribute(vehicle.set_year, 'Year')
    elif attribute == 'Make':
        _update_attribute(vehicle.set_make, 'Make')
    elif attribute == 'Model':
        _update_attribute(vehicle.set_model, 'Model')
    elif attribute == 'Color':
        _update_attribute(vehicle.set_color, 'Color')
    elif attribute == 'Mileage':
        _update_attribute(vehicle.set_mileage, 'Mileage')
    else:
        print('That attribute does not exist or cannot be modified.')

def _update_attribute(function, attribute):
    '''Use automobile setter functions to validate attribute changes'''
    while not function(input(attribute + ': ')):
        pass

def _print_sign(sign):
    '''Prints a formatted divider with a message at its center'''
    repeat = int((70 - len(sign)) / 2)
    left = ('='*repeat) + sign
    right = '='*(70 - len(left))
    print(left + right)
    print()

def menu_choice(inv, c):
    '''Maps menu option input to appropriate function calls'''
    result = True
    
    print()
    if c == '1':
        _print_sign(' Add a vehicle to inventory ')
        add_vehicle(inv)
    if c == '2':
        _print_sign(' Remove a vehicle from inventory ')
        remove_vehicle(inv)
    if c == '3':
        _print_sign(' Update a vehicle in inventory ')
        update_vehicle(inv)
    if c == '4':
        _print_sign(' View Inventory ')
        display_inventory(inv)
    if c == 'x':
        _print_sign(' Save to file ')
        save_inventory(inv)
        result = False
    
    input('\nPress enter to continue')
    
    return result

def menu(title):
    '''Displays title of program and main menu options'''
    _print_sign(title)
    print('(1) Add vehicle to inventory')
    print('(2) Remove vehicle from inventory')
    print('(3) Update a vehicle in inventory')
    print('(4) Display vehicles in inventory')
    print('-----------------------------------')
    print('(x) Save to file and exit program')
    print()

def main():
    '''Drives menu'''
    inv = InventoryClass.Inventory()
    # _seed(inv)
    
    again = True
    while(again):
        menu(' Vehicle Inventory Program ')
        again = menu_choice(inv, input('Enter an option: '))
        print()
    
    print('Goodbye!')

def _seed(inventory):
    '''Populate inventory for testing'''
    v = AutomobileClass.Automobile()
    v.create(1989, 'Toyota', 'Camry', 'rust', 201022, 'AHSH39874')
    inventory.add(v)
    
    v = AutomobileClass.Automobile()
    v.create(1999, 'Ford', 'Focus', 'green', 124222, 'A25H39273')
    inventory.add(v)
    
    v = AutomobileClass.Automobile()
    v.create(2012, 'Honda', 'Civic', 'gray', 70423, 'JHG3857FHJ')
    inventory.add(v)
    
    v = AutomobileClass.Automobile()
    v.create(2019, 'Kia', 'Forte', 'white', 20122, 'KJHSG83783')
    inventory.add(v)

main()
