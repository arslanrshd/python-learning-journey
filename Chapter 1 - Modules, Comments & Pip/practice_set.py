# ---------- Chapter 1 Practice Set ----------

# Q1: Print the Twinkle Twinkle poem
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")

# Q2: Table of 5 (same thing you will type in the REPL)
print("\nTable of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Q3: External module (installed using pip install pyfiglet)
import pyfiglet  # type: ignore

# Use the external module to print a banner
print()
print(pyfiglet.figlet_format("Python"))

# Q4: Built-in module to work with files and folders
import os

# Print contents of the current directory
print("Files in this directory:")
files = os.listdir(".")   # "." means the current folder
for f in files:
    print(f)

# Q5: This whole program is labeled with comments (see the # lines above)