#!/usr/local/bin/python3

import hashlib
import base64
import argparse

# Create the parser
my_parser = argparse.ArgumentParser(
    description='A deterministic password manager tool')

# Add the arguments
my_parser.add_argument('password',
                       metavar='password',
                       type=str,
                       help='master password')

my_parser.add_argument('service',
                       metavar='service',
                       type=str,
                       help='service name')

my_parser.add_argument('-i',
                       '--index',
                       action='store', type=int, default=0,
                       help="The index of the password for that service")

my_parser.add_argument('-l',
                       '--length',
                       action='store', type=int, default=16,
                       help="The length of the generated password")

args = my_parser.parse_args()

master_password = args.password
service = args.service
index = args.index

m_master_password = hashlib.sha512()
m_master_password.update(master_password.encode())

m_service = hashlib.sha512()
m_service.update(service.encode())

m = hashlib.sha512()
m.update(m_master_password.digest())
m.update(m_service.digest())
m.update(str(index).encode())

byte_array = m.digest()

base64_password = base64.b85encode(byte_array)
print(base64_password.decode()[:args.length])
