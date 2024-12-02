import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Punisher Skull with Sword ASCII Art
punisher_art = """
       ______
    .-        -. 
   /            \\  
  |,  .-.  .-.  ,|  
  | )(_o/  \\o_)( |  
  |/     /\\     \\|  
   (_    ^^    _)  
    \\__|IIIIII|__/  
     | \\IIIIII/ |  
     \\          /  
      `--------` 
       // || \\\\
      //  ||  \\\\
     ||   ||   ||
     ||   ||   ||
      \\\\  ||  //
       \\\\ || //
         ||||
         ||||
"""

# Text Animation Function
def animate_text(text, delay=0.2):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Main function to display the program
def birthday_program():
    os.system("clear")
    print(Fore.RED + Style.BRIGHT + punisher_art)  # Punisher art in red
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW]
    
    # Multi-color light effect
    for _ in range(5):  # Loop for light effect
        for color in colors:
            os.system("clear")
            print(color + Style.BRIGHT + punisher_art)  # Flashing skull
            time.sleep(0.1)
    
    # Display birthday message
    os.system("clear")
    animate_text(Fore.YELLOW + "HAPPY BIRTHDAY TO THE UNSTOPPABLE", 0.1)
    animate_text(Fore.CYAN + "MIDHUN", 0.2)
    animate_text(Fore.GREEN + "EMBRACE YOUR INNER PUNISHER!", 0.1)
    print(Fore.RED + Style.BRIGHT + punisher_art)

# Run the program
if __name__ == "__main__":
    birthday_program()
