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
                       help="The index of the password for that service (defaults to 0)")

my_parser.add_argument('-l',
                       '--length',
                       action='store', type=int, default=16,
                       help="The length of the generated password (defaults to 16)")

args = my_parser.parse_args()


def get_password(master_password: str, service_name: str, index=0, length=16):
    m_master_password = hashlib.sha512()
    m_master_password.update(master_password.encode())
    password = m_master_password.digest()

    m_service = hashlib.sha512()
    m_service.update(service_name.encode())
    service = m_service.digest()

    m = hashlib.sha512()

    m.update(password)
    m.update(service)
    m.update(str(index).encode())

    byte_array = m.digest()
    base64_password = base64.b85encode(byte_array)

    return base64_password.decode()[:length]


master_password = args.password
service = args.service
index = args.index
length = args.length

print(get_password(master_password, service, index=0, length=16))
