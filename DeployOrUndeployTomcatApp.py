import os
import requests
from requests.auth import HTTPBasicAuth

# Configuration
TOMCAT_HOST = "http://localhost:8080"
TOMCAT_USERNAME = "admin"
TOMCAT_PASSWORD = "password"
WAR_FILE_PATH = "/path/to/your/application.war"
APP_CONTEXT = "/myapp"  # The context path of the deployed application

# Endpoints
TOMCAT_MANAGER_DEPLOY = f"{TOMCAT_HOST}/manager/text/deploy"
TOMCAT_MANAGER_UNDEPLOY = f"{TOMCAT_HOST}/manager/text/undeploy"

def deploy_application():
    """Deploy the WAR file to Tomcat."""
    if not os.path.exists(WAR_FILE_PATH):
        print(f"Error: WAR file not found at {WAR_FILE_PATH}")
        return

    with open(WAR_FILE_PATH, 'rb') as war_file:
        files = {'war': war_file}
        params = {'path': APP_CONTEXT, 'update': 'true'}

        print("Deploying application to Tomcat...")
        response = requests.put(
            TOMCAT_MANAGER_DEPLOY,
            auth=HTTPBasicAuth(TOMCAT_USERNAME, TOMCAT_PASSWORD),
            files=files,
            params=params
        )

        if response.status_code == 200:
            print("Deployment successful.")
            print(response.text)
        else:
            print(f"Failed to deploy. HTTP Status Code: {response.status_code}")
            print(response.text)

def undeploy_application():
    """Undeploy the application from Tomcat."""
    params = {'path': APP_CONTEXT}

    print("Undeploying application from Tomcat...")
    response = requests.get(
        TOMCAT_MANAGER_UNDEPLOY,
        auth=HTTPBasicAuth(TOMCAT_USERNAME, TOMCAT_PASSWORD),
        params=params
    )

    if response.status_code == 200:
        print("Undeployment successful.")
        print(response.text)
    else:
        print(f"Failed to undeploy. HTTP Status Code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    print("Tomcat Deployment Script")
    print("1. Deploy Application")
    print("2. Undeploy Application")
    choice = input("Choose an option: ")

    if choice == "1":
        deploy_application()
    elif choice == "2":
        undeploy_application()
    else:
        print("Invalid choice. Exiting.")
