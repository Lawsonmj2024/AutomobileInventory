'''
Portfolio Project
Michael Lawson
Colorado State University, Global
ITS320: Intro to Programming
Dr. Anwar Ahmed
January 15, 2023
'''

class Automobile(object):
    '''Contains attributes and methods for objects representing an Automobile'''
    
    def __init__(self):
        '''Default constructor'''
        self._make = ''
        self._model = ''
        self._color = ''
        self._year = 0
        self._mileage = 0
        self._VIN = '' 
    
    def __str__(self):
        '''Return a formatted String composed of object attributes'''
        return str('%-17s  %-4d %-20s %-10s %7d miles' % (self._VIN, self._year, (self._make + ' ' + self._model), self._color, self._mileage))
    
    def set_make(self, make):
        '''Validate and change make of automobile'''
        # Attribute has not been modified
        result = False
        
        # Attempt to modify attribute
        try:
            # validate
            self._check_for_null(make)
            
            # modify
            self._make = make
            result = True
        
        except ValueError:
            print('Cannot be empty.')
        
        # Return True if attribute was changed, False if not
        return result
    
    def set_VIN(self, VIN):
        '''Validate and change VIN of automobile'''
        # Attribute has not been modified
        result = False
        
        # Attempt to modify attribute
        try:
            # validate
            self._check_for_null(VIN)
            if not VIN.isalnum() or len(VIN) > 17:
                raise ValueError
            
            # modify
            zeroes = 17 - len(VIN)
            self._VIN = '0'*zeroes + VIN.upper()
            result = True
        
        except ValueError:
            print('VIN must be alphanumeric and 17 characters or less.')
        
        # Return True if attribute was changed, False if not
        return result
    
    def set_model(self, model):
        '''Validate and change model of automobile'''
        # Attribute has not been modified
        result = False
        
        # Attempt to modify attribute
        try:
            # validate
            self._check_for_null(model)
            
            # modify
            self._model = model
            result = True
            
        except ValueError:
            print('Cannot be empty.')
        
        # Return True if attribute was changed, False if not
        return result
    
    def set_color(self, color):
        '''Validate and change color of automobile'''
        # Attribute has not been modified
        result = False
        
        # Attempt to modify attribute
        try:
            # validate
            self._check_for_null(color)
            
            # modify
            self._color = color
            result = True
        
        except ValueError:
            print('Cannot be empty.')
        
        # Return True if attribute was changed, False if not
        return result
    
    def set_year(self, year):
        '''Validate and change year of automobile'''
        # Attribute has not been modified
        result = False
        
        # Attempt to modify attribute
        try:
            # validate
            self._check_for_null(year)
            if int(year) < 1900 or int(year) > 9999:
                raise ValueError
            
            # modify
            self._year = int(year)
            result = True
        
        except ValueError:
            print('Invalid year.')
        
        # Return True if attribute was changed, False if not
        return result
    
    def set_mileage(self, miles):
        '''Validate and change mileage of automobile'''
        # Attribute has not been modified
        result = False
        
        # Attempt to modify attribute
        try:
            # validate
            self._check_for_null(miles)
            if int(miles) <= 0:
                raise ValueError
            
            # modify
            self._mileage = int(miles)
            result = True
        
        except ValueError:
            print('Mileage must be a positive number.')
        
        # Return True if attribute was changed, False if not
        return result
    
    def get_VIN(self):
        '''Returns VIN of automobile'''
        return self._VIN
    
    def get_make(self):
        '''Returns make of automobile'''
        return self._make
    
    def get_model(self):
        '''Returns model of automobile'''
        return self._model
    
    def get_color(self):
        '''Returns color of automobile'''
        return self._color
    
    def get_year(self):
        '''Returns year of automobile'''
        return self._year
    
    def get_mileage(self):
        '''Returns mileage of automobile'''
        return self._mileaage
    
    def _check_for_null(self, item):
        '''Raise ValueError for empty strings'''
        if(len(item) == 0 or item == None):
            raise ValueError
    
    def create(self, year, make, model, color, miles, vin):
        '''Construct vehicle for testing'''
        self._year = year
        self._make = make
        self._model = model
        self._color = color
        self._mileage = miles
        self.set_VIN(vin)
