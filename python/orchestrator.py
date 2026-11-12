import subprocess, os, json

def run_terraform():
    # Path setup 
    file_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(file_dir)
    terraform_dir = os.path.join(root_dir, 'terraform')
    print(terraform_dir)

    # Initialize Terraform
    subprocess.run(['terraform', 'init'], check=True, cwd=terraform_dir)

    # Apply the Terraform configuration
    subprocess.run(['terraform', 'apply', '-auto-approve'], check=True, cwd=terraform_dir)

     # Orchestrator gets the output from Terraform and returns it as a dictionary
    result = subprocess.run(['terraform', 'output', '-json'], check=True, capture_output=True, text=True, cwd=terraform_dir)
    print(result.stdout)

    # Parse the JSON output and return the value of the 'json_path' key
    terraform_output = json.loads(result.stdout)
    return terraform_output['json_path']['value']

if  __name__ == "__main__":
   path_to_json_file = run_terraform()
   print(f"Path to JSON file: {path_to_json_file}")