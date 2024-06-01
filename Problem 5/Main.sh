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
mkdir Evidence
cd Evidence
touch locations.txt witnesses.txt murder_weapons.txt # Create the evidence files