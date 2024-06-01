import os
import time
import subprocess

def run_script(problem_number, script_path):
  try:
    if script_path.endswith('.ps1'):
      output = subprocess.check_output(['pwsh', script_path], text=True).strip('\n')
      if output == answer_key[problem_number]:
        return True
      else:
        print(f"Try again! Your output was:\n{output}")
        return False
    else:
      output = subprocess.check_output(['bash', script_path], text=True).strip('\n')
      if output == answer_key[problem_number]:
        return True
      else:
        print(f"Try again! Your output was:\n{output}")
        return False
  except Exception as e:
    print(f"A fatal error occurred! This probably means your script couldn't even compile:\n{e}")
    return False

os.system('cls' if os.name == 'nt' else 'clear')
ascii_art = '''
.___  ___.  __    __  .______       _______   _______ .______                  
|   \/   | |  |  |  | |   _  \     |       \ |   ____||   _  \                 
|  \  /  | |  |  |  | |  |_)  |    |  .--.  ||  |__   |  |_)  |                
|  |\/|  | |  |  |  | |      /     |  |  |  ||   __|  |      /                 
|  |  |  | |  `--'  | |  |\  \----.|  '--'  ||  |____ |  |\  \----.            
|__|  |__|  \______/  | _| `._____||_______/ |_______|| _| `._____|            

.___  ___. ____    ____  _______.___________. _______ .______     ____    ____ 
|   \/   | \   \  /   / /       |           ||   ____||   _  \    \   \  /   / 
|  \  /  |  \   \/   / |   (----`---|  |----`|  |__   |  |_)  |    \   \/   /  
|  |\/|  |   \_    _/   \   \       |  |     |   __|  |      /      \_    _/   
|  |  |  |     |  | .----)   |      |  |     |  |____ |  |\  \----.   |  |     
|__|  |__|     |__| |_______/       |__|     |_______|| _| `._____|   |__|     
'''
print("\033[91m" + ascii_art + "\033[0m")

print("Press ENTER to get started.")
input()
os.system('cls' if os.name == 'nt' else 'clear')
story_text = '''
You're a seasoned detective in the Cyber Crimes Division of the FBI. 
Last night, you received a call from the local police department.
The news was chilling: someone broke into the computer lab to annihilate
all traces of a recent murder investigation from the FBI's servers. Luckily,
our forensic analysts have some leftover data that the trespasser left
behind in their wake. Will you help the FBI solve this murder mystery?
'''

print(story_text)
print("Press ENTER to continue.")
input()
os.system('cls' if os.name == 'nt' else 'clear')

instructions_text = '''
Each problem you solve reveals a piece of the puzzle, bringing you closer to identifying the culprit.

Here's how to get started:
1. Enter the directory for current problem you are working on.
2. Edit the PowerShell/Bash script for the problem.
3. Check whether the output of the script is corrcect!
'''

print(instructions_text)
print("Press ENTER to continue.")
input()
os.system('cls' if os.name == 'nt' else 'clear')

problems_list = '''
PowerShell Problems (Windows Server):
1. Last Location
2. Murder Weapon
3. Locked Out

Bash Problems (Linux Server):
4. Physical Appearance
5. Records Cleanup
6. Suspect Age
'''

documents_directory = {
    1: "doc/1",
    2: "doc/2",
    3: "doc/3",
    4: "doc/4",
    5: "doc/5",
    6: "doc/6"
}

problems_directory = {
    1: "Problem 1",
    2: "Problem 2",
    3: "Problem 3",
    4: "Problem 4",
    5: "Problem 5",
    6: "Problem 6"
}

answer_key = {
    1: "1236",
    2: "Dagger",
    3: "Fbir0Ck$!",
    4: "Physical appearance: suspect is a tall man with black apparel.",
    6: "34"
}

correct_status = {
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
}

final_text = '''
It's time to solve this murder mystery once and for all.
We have the murderer's identity as an encrypted Blowfish hash via CBC (cipher block chaining):
Csn2rzR50ISy6MBvjCZv/w==

The key to solve this hash is the combination of answers for questions 1-4 and 6 
in all lowercase while only including alphanumeric characters and excluding spaces.
'''

while True:
  try:
    flag = False
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in problems_list.splitlines():
        if line != '' and line[0].isnumeric() and correct_status[int(line[0])]:
            line += " ✅"
        print(line)
    choice = input("Choose a problem number to access (or m for the final challenge): ")
    if (choice == "m"):
      if all(correct_status[i] for i in range(1, 7)):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(final_text)
        while True:     
          response = input("What is the full name of the murderer? Include proper spacing and capitalization. (b to back)\n").strip()
          if response == 'Dobromir Iliev':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("CONGRATULATIONS ON SOLVING THE MURDER MYSTERY!\nSee an officer ASAP to claim the prize!")
            time.sleep(100000000000000)
          elif response.lower() == 'b':
            flag = True
            break
          else:
            print("Try again!")
            continue
      else:
        print("You haven't finished all of the problems yet!")
        continue
    elif not choice.isnumeric():
      print("Please enter a valid problem number or m for the final challenge.")
      continue
    if flag:
      continue
    choice = int(choice)
    selected_problem_path = problems_directory.get(choice)
    selected_document_path = documents_directory.get(choice)
    if correct_status[choice] == True:
        print("You have already solved this problem!")
        time.sleep(1)
        continue
    if not all(correct_status[i] for i in range(1, 4)):
        if choice in [4, 5, 6]:
            print("\nYou must solve problems 1-3 to get access to the Linux Server!")
            time.sleep(1.5)
            continue
    if selected_problem_path and os.path.exists(selected_problem_path):
      os.system('cls' if os.name == 'nt' else 'clear')
      with open(selected_document_path, "r") as f:
        print(f.read())
      while True:
        try:
          if choice != 6 and choice != 5:
            choice2 = input("\nPress r to run the script for this problem! (or b to go back): ")
            if choice2.lower() == "b":
              break
            if choice2.lower() == "r":
              if choice in [1, 2, 3]:
                if os.path.exists((selected_problem_path + "/Main.ps1")):
                    if (run_script(choice, selected_problem_path + "/Main.ps1") is True):
                        print("Correct!")
                        correct_status[choice] = True
                        time.sleep(1.5)
                        break
              elif choice in [4]:
                if os.path.exists((selected_problem_path + "/Main.sh")):
                    if (run_script(choice, selected_problem_path + "/Main.sh") is True):
                        print("Correct!")
                        correct_status[choice] = True
                        time.sleep(1.5)
                        break
              else:
                print("Missing script file for this problem!")
          elif choice == 6:
            while True:
              answer = input("Enter your answer (or b to go back):")
              if answer.strip() == answer_key.get(choice):
                print("Correct!")
                correct_status[choice] = True
                time.sleep(1.5)
                break
              elif (answer == "b"):
                    break
              else:
                print("Please try again in 30 seconds.")
                time.sleep(30)
            break
          elif choice == 5:
            choice2 = input("\nPress r to check this problem! (or b to go back): ")
            if choice2.lower() == "b":
              break
            if choice2.lower() == "r":
                if (not os.path.exists("Problem 5/The records of a deranged Cybersecurity Officer") and os.path.exists("Problem 5/FBI Records") and os.path.exists("Problem 5/FBI Records/Suspects") and os.path.exists("Problem 5/FBI Records/Evidence") and os.path.exists("Problem 5/FBI Records/Suspects/names.txt") and os.path.exists("Problem 5/FBI Records/Evidence/witnesses.txt") and os.path.exists("Problem 5/FBI Records/Evidence/murder_weapons.txt") and os.path.exists("Problem 5/FBI Records/Evidence/locations.txt")):
                  print("Correct!")
                  correct_status[choice] = True
                  time.sleep(1.5)
                  break
                else:
                  print("The FBI Records folder isn't properly structured! Please try again.")
            else:
                print("Please enter a valid option.")
          else:
            print("Please enter a valid choice.")
        except:
          print("Invalid input. Please run the problem's script or go back.")
    else:
      print("Invalid choice or problem unavailable. Please try again.")
  except:
    print("Please enter a valid problem number or m to go to the final challenge.")
