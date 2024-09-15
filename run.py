import subprocess

# List of commands to execute
commands = [
    "echo 1 > /proc/sys/net/ipv4/ip_forward",
    "iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000",
    "iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53"
]

# Execute each command in sequence
for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Command executed successfully: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing command: {e}")