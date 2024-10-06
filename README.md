## PowerShell/Bash Murder Mystery Koan

![image](https://github.com/user-attachments/assets/9edeb995-e2a2-4530-97fa-e986da7eba6a)

## Overview
The Bash/PowerShell Murder Mystery Koan is an engaging series of programming challenges designed to teach participants the fundamentals of PowerShell and Bash scripting. This educational tool was developed as part of a workshop aimed at training CyberDragons team members in essential scripting skills through an interactive murder mystery scenario.

## Getting Started

### Prerequisites

1. **Clone the Repository**  
   Start by cloning this repository to your local machine and cd'ing into it:
   ```bash
   git clone https://github.com/GSMSTCSClub/PowerShell-and-Bash-Murder-Mystery-Koan
   cd PowerShell-and-Bash-Murder-Mystery-Koan
   ```

2. **Obfuscate the Python Script**  
   Before distributing the project, ensure that the Python file is obfuscated to prevent participants from accessing the original source code. Use **pyarmor** for this:
   ```bash
    pyarmor gen main.py
   ```

3. **Distribute the Obfuscated File and Pyarmor Runtime**  
   The resulting obfuscated binary and a runtime directory will be located in the `dist/` directory. You must distribute the pyarmor runtime directory and obfuscated python file to all workshop participants.

4. **Run the Murder Mystery**  
   To start the murder mystery, execute the following command:
   ```bash
   python3 main.py
   ```
   Keep in mind that `main.py` should be the obfuscated version generated by pyarmor. Note that both Bash (`bash`) and PowerShell (`pwsh`) binaries are required to complete the challenges.

5. **Solve the murder mystery!**
   Go through the menus, test running the code, and solve the challenges!
   
   ![image](https://github.com/user-attachments/assets/55dd33c8-6a38-496b-8117-5ddd80801b22)

## Recommended Environment

- **Local Machine or SSH to Linux**: In the workshop itself, we used Replit with the PowerShell package, but it was extremely slow. For future workshops, it's highly recommended to work in a local environment, such as a Linux system with PowerShell installed.
- **Python Version**: Ensure that you are using Python 3.11 or later, as Pyarmor does not support versions below 3.10.


## Challenge Structure

Each challenge in this series requires thoughtful problem-solving, often necessitating more than basic scripting knowledge. To assist participants without discouraging them, we recommend providing boilerplate code with incomplete sections that require their implementation. 

## Common Issues
If a workshop participant can't run the obfuscated python script or run their code:
- Their python might be out of date
- They might not have Powershell or Bash on their system
- They may have deleted the pyarmor runtime, or the pyarmor runtime is not in the same working directory as the obfuscated python script
- They might have deleted the template files, which must be named "Main" and then the corresponding file extension (`ps1` for PowerShell and `sh` for Bash)
- They could have accidentally deleted or renamed any of the directories for the Koan, such as a directory for one of the problems, or the `doc` directory for the READMEs

## Answer Key

### Question I — Last Known Location
```
The file mystery.log contains vital information about the murder.
The log is formatted as follows, with one log per line:
"LOG #<LOGNUMBER> DATE: <YYYY-MM-DD> <HH:MM:SS> ACTIVITY: <ACTIVITY> LOCATION: <LOCATION> DETAILS: <DETAILS>"

What is the log number of the log containing the last known location of the murder? 
  
The log contains the activity "Last Known Location" followed by the murderer's address in the "LOCATION" field.
Make sure to use PowerShell to determine your answer! Only provide the number and nothing else.
```

```pwsh
Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)
Get-Content -Path "mystery.log" | Where-Object { $_ -match "ACTIVITY: Last Known Location" } | ForEach-Object { $_ -match "LOG #(\d+)" | Out-Null; $matches[1] } # 1236
```

### Question II — Murder Weapon
```
The murderer hid all the information related to the murder weapon in the password-protected zip file enc.zip.
We believe they used the street name of their address as the password for the zip.
You will have to extract the contents of the zip file!

Once you have extracted the zip file, we need you to figure out the following using PowerShell:
what is the name of the weapon the murderer used?
```

```pwsh
Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)

$weaponIds = Get-Content -Path weapon-ids
$weaponNames = Get-Content -Path weapon-names
$weaponUsed = Get-Content -Path weapon-used

$index = $weaponIds.IndexOf($weaponUsed)
$weaponName = $weaponNames[$index]
Write-Output $weaponName # "Dagger"
```

### Question III — Locked Out
```
The murderer locked us out of our Linux server! The password to unlock the server is contained within
the file secret, but it looks like gibberish! Can you help us figure it out?

Decrypt and print out the password using PowerShell. Make sure you preserve the casing of the password!
```

You are basically being asked to implement ROT13 in PowerShell for this problem.
```pwsh
# Set the current location to the directory of the script
Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)

# Read from the file 'secret' and store it in $secret
$secret = Get-Content -Path secret

function Rotate-Char($char) {
    $ascii = [int]$char

    
    if ($char -match '[a-zA-Z]') { # Check if the character is a letter
    # Subtract 97 if capitalized and 65 otherwise to get letter indices
        $offset = if ($char -cmatch '[a-z]') { 97 } else { 65 }
    # ROT13_index = (letter_index+13) mod 26
        $rotatedAscii = ($ascii - $offset + 13) % 26 + $offset
        [char]$rotatedAscii
    } else {
        $char # Otherwise, return the original character
    }
}

# Calls the Rotate-Char function for each character
$rot13Secret = -join ($secret.ToCharArray() | ForEach-Object {
   Rotate-Char $_
})

$finalSecret = ($rot13Secret -split '\s+')[3] # We don't care about the first three words

Write-Output $finalSecret # "Fbir0Ck$!"
```

### Question IV — Physical Appearance
```
We need to look through for more information on the suspect.
Lucky for us, the FBI has a database we can use! Unfortunately, it's filled with a bunch of gibberish.
We know there's a file in the database containing the suspect's physical appearance, but searching for
it manually would take too long... it's up to you to figure it out.

Using Bash, what is the contents of the file?
```

```bash
cd "$(dirname $0)"/FBI\ Data\ base\ xD/Funny\ Murder\ Case # cd to "Funny Murder Case"
cat FJ1I23183D.txt # print the file contents of the suspicious file (use grep -r to find it in the first place)
```

### Question V — Records Cleanup
```
Oh no! The murderer deleted our investigation records! We need your help. Please do the following:
1. Change the directory name back to "FBI Records"
2. They zip bombed our folder. You need to delete all the junk folders.
3. We need to establish new records for this case ASAP! Create files and folders in "FBI Records" as follows:

FBI Records
├── Evidence
│   ├── locations.txt
│   ├── murder_weapons.txt
│   └── witnesses.txt
└── Suspects
    └── names.txt

This problem only checks whether the appropriate folders/files exist and are properly named, but you are still
expected to run a script that automatically creates the specified file structure. You must use scripting tools
for this; don't cheat by creating the files and directories manually!

NOTE: The contents of the evidence files are left intentionally ambiguous. You are NOT required to fill them with data.
```

```bash
# Set current directory to the script's location
cd "$(dirname "$0")"

# Use the mv (move) command to change the directory name
mv "The records of a deranged Cybersecurity Officer" "FBI Records"
cd "FBI Records" # Change directory into the FBI Records folder
rm -rf * # Remove all files in the records folder
mkdir Suspects # Create the Suspects directory
cd Suspects # Change directory into the Suspects folder
touch names.txt # Create the names.txt file
cd .. # Change directory back to the FBI Records folder
mkdir Evidence # Create the Evidence directory
cd Evidence # Change directory into the Evidence folder
touch locations.txt witnesses.txt murder_weapons.txt # Create the evidence files
```

### Question VI — Suspect Age
```
We are so close to solving this mystery!
We need to find the suspect's age hidden in this super duper omega cool shady computer directory.

What is the suspect's age in years?

NOTE: This problem doesn't run a script; you must enter the answer manually.
```

Run `tree -a` to recursively view the hidden files in the current working directory:
```
❯ tree -a
.
├── .keysInfo.txt
├── .keys.txt
└── Secret Folder
    └── Super Secret Folder
        └── Super Duper Secret Folder
            └── Super Duper Mega Secret Folder
                └── Ultra Mega Secret Folder
                    ├── .enc
                    └── THE SECRET
                        └── Answer.txt
```

The output of `Answer.txt` is a red herring but gives a pretty good hint on the problem:
```
❯ cat Secret\ Folder/Super\ Secret\ Folder/Super\ Duper\ Secret\ Folder/Super\ Duper\ Mega\ Secret\ Folder/Ultra\ Mega\ Secret\ Folder/THE\ SECRET/Answer.txt
Are you a silly goose? Did you really think we would hide the answer right here??
IDK maybe what you're looking for is some kind of file. Perhaps a hidden file?
```

So, we look for hidden files. The outputs of `.enc`, `.keysInfo.txt`, and `.keys.txt` are:
```
❯ cat Secret\ Folder/Super\ Secret\ Folder/Super\ Duper\ Secret\ Folder/Super\ Duper\ Mega\ Secret\ Folder/Ultra\ Mega\ Secret\ Folder/.enc
Ecj exdkjow tn ytlcod-rrfm dqdcn txg.
```
```
❯ cat .keysInfo.txt
Oh no! Theres too many different keys to test out!
Maybe the real one is a mistake only a L officer could make.

...something only Andrew Zeng would do
```
```
❯ cat .keys.txt
definitely the key: BaDydKKa13
probably the key: Kg2ooaAorr
definitely the key: 47kHt70dJ8
definitely the key: D9zolzzAlo
probably the key: Yyek6Ez6AS
definitely the key: hHnXHe2YU9
definitely the key: AB8PoIgUvQ
definitely the key: xoQNEO6EHT
ZA KEY: DNLUafwkXK
ZA KEY: oj2OjMgGun
definitely the key: mPE4aJ0FHY
definitely the key: zPUM1IucpI
definitely the key: RpSSLabTec
probably the key: RmrfZfSuUf
probably the key: v7882YLwi1
...
```

So it becomes a decryption problem. The key for `enc` is in `.keys.txt`, and it is a [Vigenere Cipher](https://www.dcode.fr/vigenere-cipher)
```
❯ grep "Andrew" .keys.txt
Common Andrew Zeng L: lvfmd
```

![image](https://github.com/user-attachments/assets/18881dbf-7b51-4e3d-b4d8-aac1e3232a76)

### Final Challenge
```
It's time to solve this murder mystery once and for all.
We have the murderer's identity as an encrypted Blowfish hash via CBC (cipher block chaining):
Csn2rzR50ISy6MBvjCZv/w==

The key to solve this hash is the combination of answers for questions 1-4 and 6 
in all lowercase while only including alphanumeric characters and excluding spaces.
```

Use an [online Blowfish decrypter](https://sladex.org/blowfish.js/). The key is:
```
1236daggerfbir0ckphysicalappearancesuspectisatallmanwithblackapparel34
```

![image](https://github.com/user-attachments/assets/44ee8039-0b03-4d22-bb1d-0bf5f9ab4f1e)

**So the murderer was *Dobromir Iliev!***
