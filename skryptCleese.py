import sys

def customized_hello(prefix, first_name, last_name):
    print("Hello %s %s %s!" % (prefix, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 5:
        exit(1)
    first_name = sys.argv[2]
    last_name = sys.argv[3]
    prefix = sys.argv[1]
    customized_hello(prefix, first_name, last_name)