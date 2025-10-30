#version with 2 Modes
import random

def load_names(language, gender):
    """Load names from local text files in '/data' based on language and gender."""
    file_path = f"data/{language}_{gender}.txt"    
    names = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    return names


def load_second_names(language):
    file_path = f"data/{language}_SN.txt"
    second_names = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            second_names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Warning: Second name file not found: {file_path}")
    return second_names


def extend_name(first_name, second_names=None):
    variations = []

    
    variations.append(first_name.lower())
    variations.append(first_name.upper())
    variations.append(first_name.capitalize())

    
   # for i in range(0, 100):
       # variations.append(f"{first_name}{i}")

    
    for year in range(1970, 2027):
        variations.append(f"{first_name}{year}")

   
   # variations.append(f"_{first_name}")
    #variations.append(f"{first_name}_")

    
    if second_names:
        for sn in second_names:
            variations.append(f"{first_name}_{sn}")
            #variations.append(f"_{first_name}_{sn}")
            #variations.append(f"{first_name}_{sn}_")
            #variations.append(f"{sn}_{first_name}")

    return variations

############################## MODE 2 #############################################
def extend_name_mode2(first_name, second_name=None, second_names_list=None):
    variants = []

    # Basic case variations
    variants.append(first_name.lower())
    variants.append(first_name.upper())
    variants.append(first_name.capitalize())

    
    leet = first_name.replace('a','@').replace('e','3').replace('i','1').replace('o','0').replace('s','$')
    if leet != first_name:
        variants.append(leet)

    
    for i in range(1, 100):
        variants.append(f"{first_name}{i}")
        variants.append(f"{i}{first_name}")

    for year in range(1970, 2027):
        variants.append(f"{first_name}{year}")

    
    if second_name:
        variants.append(f"{first_name}{second_name}")
        variants.append(f"{second_name}{first_name}")
        variants.append(f"{first_name}.{second_name}")
        variants.append(f"{second_name}.{first_name}")

    
    if second_names_list:
        for sn in second_names_list:
            variants.append(f"{first_name}_{sn}")
            variants.append(f"{sn}_{first_name}")

    return list(set(variants))  



print("This tools will create a wordlist that can be used for both User and password fields.\n"
      "Choose Mode 1 - 'Scope' if you want to make a scoped wordlist\nChoose Mode 2 - 'Laser' if you know the target name and/or surname")

print("Select Mode:\n1 - Scope Mode\n2 - Laser Mode (Known name)")
mode = input(" > ").strip()

if mode not in ("1", "2"):
    print("Error: Invalid mode. Exiting.")
    exit()



if mode == "2":
   
    first_name = input("Enter first name: ").strip()
    if not first_name:
        print("Error: First name required. Exiting.")
        exit()

    second_name = input("Enter surname (press Enter if unknown): ").strip()

    second_names_list = None
    if not second_name:
        
        print("Select Language Type for surname list:\n1 - UK English\n2 - US English\n3 - Spain Spanish\n4 - LATAM Spanish")
        ListType = input(" > ").strip()
        valid_languages = {"1": "UK English", "2": "US English", "3": "Spain Spanish", "4": "LATAM Spanish"}
        if ListType not in valid_languages:
            print("Invalid language. Exiting.")
            exit()
        second_names_list = load_second_names(ListType)
        if not second_names_list:
            print("No surnames loaded. Exiting.")
            exit()

    
    all_names = extend_name_mode2(first_name, second_name, second_names_list)
    random.shuffle(all_names)

   
    with open(f"{first_name}_wordlist.txt", "w", encoding="utf-8") as f:
        for name in all_names:
            f.write(name + "\n")

    print(f"Names generated and saved to {first_name}_wordlist.txt")
    exit()

##########################################################################################################

print("To make a more efficient list, narrow the scope if next fields are known about the target user:")
print("Select Language Type:\n1 - UK English\n2 - US English\n3 - Spain Spanish\n4 - LATAM Spanish")
ListType = input(" > ").strip()

print("Select Gender:\nM - Male\nF - Female")
Gender = input(" > ").upper().strip()

#print("Select Wordlist Size:\n1 - Small\n2 - Medium\n3 - Large\n4 - Extra")
print("Note: Estimated size:\n1 - Small = ~ 2 MB\n2 - Medium = ~ 19 MB\n3 - Large = ~ 950 MB\n4 - Extra = ~ 2.8 GB")
Size = input(" > ").strip()


valid_languages = {"1": "UK English", "2": "US English", "3": "Spain Spanish", "4": "LATAM Spanish"}
valid_genders = {"M": "Male", "F": "Female"}
valid_sizes = {"1": "Small", "2": "Medium", "3": "Large", "4": "Extra"}

if ListType not in valid_languages or Gender not in valid_genders or Size not in valid_sizes:
    print("Error: Invalid option entered. Please restart the program.")
    exit()

print(f"\nYou selected {valid_languages[ListType]}, {valid_genders[Gender]}, {valid_sizes[Size]} list.\n")


size_map = {
    "1": 1000,    
    "2": 10000,    
    "3": 500000,    
    "4": 1500000    # Extra
}

target_size = size_map[Size]

names = load_names(ListType, Gender)
if not names:
    print("No first names loaded. Exiting.")
    exit()


second_names = load_second_names(ListType)
all_names = []
total = len(names)
for idx, name in enumerate(names, start=1):
    all_names.extend(extend_name(name, second_names))

    
    if idx % max(1, total // 10) == 0 or idx == total:
        percent = int((idx / total) * 100)
        print(f"Progress: {percent}% ({idx}/{total} names processed)")


all_names = list(set(all_names))
if len(all_names) > target_size:
    all_names = random.sample(all_names, target_size)

#random.shuffle(all_names)

with open("scoped_wordlist.txt", "w", encoding="utf-8") as f:
    for name in all_names:
        f.write(name + "\n")

print(f"Names generated and saved to scoped_wordlist.txt")
