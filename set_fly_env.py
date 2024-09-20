import os
import subprocess
from dotenv import dotenv_values

## go to ./src
# os.chdir(os.path.join(os.path.dirname(__file__), 'src'))

# Step 1: Load environment variables from the .env file
env_vars = dotenv_values('.env')

# Step 2: Loop through each key-value pair and execute the command
for key, value in env_vars.items():
    # Construct the command to set the secret
    print(f"setting {key}")
    command = f"fly secrets set {key}={value}"
    
    # Step 3: Execute the command using subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Step 4: Check and print the result
    if result.returncode == 0:
        print(f"Successfully set {key}.")
    else:
        print(f"Failed to set {key}. Error:")
        print(result.stderr)