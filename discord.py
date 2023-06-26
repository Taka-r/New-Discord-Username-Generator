import requests
import time
import string
import random

def generate_usernames(length):
    characters = string.ascii_lowercase + string.digits + '._'
    usernames = []

    while True:  # Boucle infinie pour une génération continue
        username = ''.join(random.choice(characters) for _ in range(length))
        usernames.append(username)
        yield username

def extract_data(username):
    url = f'https://api.lixqa.de/v3/discord/pomelo/{username}'
    response = requests.get(url)
    data = response.json()

    extracted_data = data.get('data', {})
    return extracted_data

def main():
    username_length = int(input("Entrez la longueur des noms d'utilisateur : "))
    usernames = generate_usernames(username_length)

    counter = 0
    with open('username_data.txt', 'w') as file:
        while True:  # Boucle infinie pour une génération continue
            counter += 1
            username = next(usernames)
            extracted_data = extract_data(username)
            
            if 'USERNAME_ALREADY_TAKEN' not in extracted_data.get('check', {}).get('errors', []):
                result = f'{username}: {extracted_data} (#{counter})'
                file.write(result + '\n')
                print(result)

            time.sleep(5)  # Pause de 5 secondes entre chaque vérification

if __name__ == '__main__':
    main()
