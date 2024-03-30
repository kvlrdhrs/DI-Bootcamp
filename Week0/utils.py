import subprocess
import platform

def unzip_with_7z(zip_file_path, dest_path, password):
    os_type = platform.system()
    
    if isinstance(password, bytes):
        password = password.decode('utf-8')
    
    cmd_output = ""
    
    if os_type == 'Darwin':  # macOS
        result = subprocess.run(['7za', 'x', '-p' + password, '-o' + dest_path, zip_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        cmd_output = result.stdout + result.stderr
    elif os_type == 'Windows':  # Windows
        result = subprocess.run(['7z', 'x', '-p' + password, '-o' + dest_path, zip_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        cmd_output = result.stdout + result.stderr
    elif os_type == 'Linux':  # Linux
        result = subprocess.run(['7z', 'x', '-p' + password, '-o' + dest_path, zip_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        cmd_output = result.stdout + result.stderr
    else:
        print(f"Unsupported OS type: {os_type}")
        return False

    if "Everything is Ok" in cmd_output:
        print(f"Successfully extracted all files to {dest_path} with password {password}")
        return True
    else:
        return False
