import requests

def get_character_info(character_id):
    url = f"https://swapi.dev/api/people/{character_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        character_data = response.json()
        print("Character Information:")
        print("Name:", character_data["name"])
        print("Height:", character_data["height"])
        print("Mass:", character_data["mass"])
        print("Hair color:", character_data["hair_color"])
        print("Eye color:", character_data["eye_color"])
    else:
        print("Error:", response.status_code)

def main():
    character_id = input("Enter a character ID (1-88): ")
    get_character_info(character_id)

if __name__ == '__main__':
    main()

