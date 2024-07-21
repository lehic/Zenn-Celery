# import os
# from google.cloud import secretmanager

# def access_secret_version(project_id, secret_id, version_id="latest"):
#     client = secretmanager.SecretManagerServiceClient()
#     name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
#     response = client.access_secret_version(request={"name": name})
#     return response.payload.data.decode("UTF-8")

# def load_secrets_to_env(secret_data):
#     lines = secret_data.split('\n')
#     for line in lines:
#         if line.strip():  # Ignore empty lines
#             key, value = line.split('=', 1)
#             os.environ[key] = value
#             print(key, value)

# if __name__ == "__main__":
    
#     # project_id = "weareinto-staging"
#     project_id = "weareinto-staging"
#     secret_id = "staging_env_vars"
    
#     # Fetch the secret from Secret Manager
#     secret_data = access_secret_version(project_id, secret_id)
    
#     # Load secrets into environment variables
#     load_secrets_to_env(secret_data)


import os
from google.cloud import secretmanager

def access_secret_version(project_id, secret_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def save_secrets_to_env_file(secret_data, file_path=".env"):
    with open(file_path, 'w') as env_file:
        lines = secret_data.split('\n')
        for line in lines:
            if line.strip():  # Ignore empty lines
                key, value = line.split('=', 1)
                env_file.write(f"{key}={value}\n")
                print(key, value)  # For debugging purposes

if __name__ == "__main__":
    project_id = "weareinto-staging"
    secret_id = "api_workers_secrets"
    
    # Fetch the secret from Secret Manager
    secret_data = access_secret_version(project_id, secret_id)
    
    # Save secrets to .env file
    save_secrets_to_env_file(secret_data)
