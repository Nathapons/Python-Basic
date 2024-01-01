if __name__ == '__main__':
    """
    How to convert data
    variable = convertor(value)
    
    convertor = int, float, bool, list, set, tuple
    """
    x = int(1)
    x = float(1)
    x = str(2)
    
    x = bool(0)
    x = bool(1)
    
    
    # 1.The boolean value is False when the data which is converted is blank or 0
    x = bool(0)
    x = bool([])
    x = bool('')
    x = bool({})
    
    # 2. The boolean value is True when the data which is coverted is not blank and not 0
    x = bool(-1)
    x = bool(10)
    x = bool('x')
    x = bool([[]])
    