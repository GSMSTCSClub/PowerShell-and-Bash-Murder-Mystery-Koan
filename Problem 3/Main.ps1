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

Write-Output $finalSecret # Prints Fbir0Ck$!