import subprocess


def insecure_call():
    subprocess.Popen("ls -l", shell=True)  # Bandit flags shell=True as insecure


def unsafe_eval(data):
    eval(data)  # Bandit flags eval usage as insecure


password = "my_secret_password"  # Bandit catches hardcoded passwords
