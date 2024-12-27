import os
import subprocess

def install_apache():
    """Install Apache Web Server."""
    print("Updating package repository...")
    subprocess.run(["sudo", "apt-get", "update"], check=True)

    print("Installing Apache...")
    subprocess.run(["sudo", "apt-get", "install", "-y", "apache2"], check=True)

    print("Starting Apache service...")
    subprocess.run(["sudo", "systemctl", "start", "apache2"], check=True)

    print("Enabling Apache to start on boot...")
    subprocess.run(["sudo", "systemctl", "enable", "apache2"], check=True)

    print("Apache installation and configuration completed.")

def configure_apache():
    """Configure Apache Web Server."""
    print("Creating a custom configuration file...")
    config_content = """
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
"""

    config_path = "/etc/apache2/sites-available/000-default.conf"

    with open("temp_apache_config.conf", "w") as temp_config:
        temp_config.write(config_content)

    print("Updating Apache configuration...")
    subprocess.run(["sudo", "mv", "temp_apache_config.conf", config_path], check=True)

    print("Restarting Apache service...")
    subprocess.run(["sudo", "systemctl", "restart", "apache2"], check=True)

if __name__ == "__main__":
    print("Apache Installation and Configuration Script")
    print("1. Install Apache")
    print("2. Configure Apache")
    print("3. Install and Configure Apache")
    choice = input("Choose an option: ")

    if choice == "1":
        install_apache()
    elif choice == "2":
        configure_apache()
    elif choice == "3":
        install_apache()
        configure_apache()
    else:
        print("Invalid choice. Exiting.")
