import random
import string

def generate_random_string (lenght):
    random_string = ''.join([random.choice(string.ascii_letters) for _ in range(lenght)])
    
    return random_string

def generate_random_number (lenght):
    random_number = ''.join([random.choice(string.digits) for _ in range(lenght)])
    #print("ceva")
    return random_number
