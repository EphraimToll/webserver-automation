import subprocess, os

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

if __name__ == "__main__":
    run_terraform()