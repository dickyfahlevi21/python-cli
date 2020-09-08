import click
from src.hello import *
from src.a_string_trans import *
from src.b_arithmethic import *
from src.c_statistic import *
from src.d_palindrome import *
from src.e_obfuscator import *
from src.g_ip import *
from src.h_ip_eks import *


@click.group()
def cli():
    pass

# Test Hello World
cli.add_command(hello)
# 1. String Transformation
cli.add_command(upper)
cli.add_command(lower)
cli.add_command(capital)
# 2. Arithmetic
cli.add_command(add)
cli.add_command(subtract)
cli.add_command(multiply)
cli.add_command(divide)
# 3. Statistic
cli.add_command(mean)
cli.add_command(median)
cli.add_command(mode)
cli.add_command(fmean)
# 4. Palindrome
cli.add_command(is_palindrome)
# 5. Obfuscator
cli.add_command(obfuscator)
# 7. Internal IP
cli.add_command(ip_internal)
# 7. Eksternal IP
cli.add_command(ip_eksternal)


if __name__ == "__main__":
    cli()

# How to Run

# main hello
# main lowercase "I aM CrAzY TeXT"
# main uppercase "I aM CrAzY TeXT"
# main capital "I aM CrAzY TeXT"
# main add 1 4 5 2 3
# main subtract 10 2 4
# main multiply 3 5 8
# main divide 100 5 2
# main mean 90 80 77 45 32 45
# main median 10 2 4 5 9 12
# main mode 3 5 8 0 9 8 3 0 8
# main fmean 100 53 28 90 130
# main palindrome "Saya ingin pergi ke pasar"
# main palindrome "Kasur ini rusak"
# main obfuscator "email@example.com"
# main ip_internal
# main ip_eksternal