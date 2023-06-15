#!/usr/bin/env python3
import sys
print("Hola mundo!")

if __name__ == "__hello__":
    print(f"Argumentos:{len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argumento{i:<6}: {arg}")