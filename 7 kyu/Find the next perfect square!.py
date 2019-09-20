def find_next_square(sq):
    return (pow(sq, 0.5)+1)**2 if pow(sq, 0.5).is_integer() else -1
