import mysql.connector
import paramiko

def fetch_services():
    conn = mysql.connector.connect(
        host='localhost',
        user='your_user',
        password='your_password',
        database='your_db'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT service_name, node_ip, check_command FROM service_mapping")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def check_service(ip, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username='your_ssh_user', password='your_ssh_password')
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        ssh.close()
        return "Active" if "active" in output.lower() else "Inactive"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    services = fetch_services()
    for service, ip, command in services:
        status = check_service(ip, command)
        print(f"{service} on {ip} — {status}")

