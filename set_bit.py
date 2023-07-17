def set_bit(number, bit_position):
    result = 0  

    
    result |= (1 << number)

   
    result |= (1 << bit_position)

    return result
number=int(input("enter the number: "))
bit_position=int(input("enter bits_position_to_change: "))

print(set_bit(number, bit_position))