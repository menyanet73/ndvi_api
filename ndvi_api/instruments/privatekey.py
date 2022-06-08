from core.config import config, PRIVATEKEY


def create_privatekey_file():
    project_id = config('EE_PROJECT_ID')
    private_key_id = config('EE_PRIVATE_KEY_ID')
    private_key = config('EE_PRIVATE_KEY')
    client_email = config('EE_CLIENT_EMAIL')
    client_id = config('EE_CLIENT_ID')

    data = (
        f'{{\n  "type": "service_account",\n'
        f'  "project_id": "{project_id}",\n'
        f'  "private_key_id": "{private_key_id}",\n'
        f'  "private_key": "{private_key}",\n'
        f'  "client_email": "{client_email}",\n'
        f'  "client_id": "{client_id}",\n'
        f'  "auth_uri": "https://accounts.google.com/o/oauth2/auth",\n'
        f'  "token_uri": "https://accounts.google.com/o/oauth2/token",\n'
        f'  "auth_provider_x509_cert_url":'
        f'  "https://www.googleapis.com/oauth2/v1/certs",\n'
        f'  "client_x509_cert_url":'
        f'  "https://www.googleapis.com/robot/v1/metadata/x509/{client_email}"'
        f'\n}}'
    )

    with open(PRIVATEKEY, 'w') as file:
        file.write(data)
