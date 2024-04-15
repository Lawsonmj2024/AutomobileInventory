'''
Portfolio Project
Michael Lawson
Colorado State University, Global
ITS320: Intro to Programming
Dr. Anwar Ahmed
January 15, 2023
'''

class Inventory(object):
    '''Class operates dictionary data structure containing Automobiles'''

    def __init__(self):
        '''Default constructor initializes dictionary'''
        self._inventory_dict = {}
    
    def __len__(self):
        '''Return size of list'''
        return len(self._inventory_dict)
        
    def add(self, vehicle):
        '''Add a vehicle to list'''
        # Vehicle isn't added to inventory yet
        result = False 
        
        # Attempt to add vehicle to inventory
        try:
            self._inventory_dict.update({vehicle.get_VIN(): vehicle})
            result = True
        except:
            print("Vehicle was not added to inventory")
        
        # Return True if vehicle was added, False if not
        return result
    
    def remove(self, vehicle):
        '''Remove a vehicle from list'''
        # Vehicle isn't added to inventory yet
        result = False
        
        # Attempt to remove vehicle from inventory
        try:
            self._inventory_dict.pop(vehicle.get_VIN())
            result = True
        except KeyError:
            print("Vehicle not found in inventory")
            
        # Return True if vehicle was removed, False if not
        return result
    
    def display(self):
        '''Print contents of dictionary to console'''
        for veh in self._inventory_dict.values():
            print(str(veh))
    
    def find_vehicle(self, VIN):
        '''Locate a VIN in dictionary, return Automobile object if found, None if not found'''
        return self._inventory_dict.get(VIN, None)
    
    def is_empty(self):
        '''Checks if dictionary is empty'''
        result = len(self._inventory_dict) == 0
        if result:
            print('There are not any vehicles in the inventory.')
        return result
    
    def save_to_file(self, head, filename):
        '''prints inventory to a file'''
        file = open(filename, 'w')
        file.write(head)
        
        for vehicle in self._inventory_dict.values():
            file.write(str(vehicle) + "\n")
        
        file.close()