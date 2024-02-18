import requests
import random
import time

def create_short_link(url, unique_id):
    url_with_param = f"{url}?id={unique_id}"
    api_url = "https://tinyurl.com/api-create.php?url=" + url_with_param
    response = requests.get(api_url)
    return response.text if response.status_code == 200 else None

def main(input_file, output_file, n):
    hotdog_url = "https://en.wikipedia.org/wiki/Hot_dog"
    unique_game_id = int(time.time())

    with open(input_file, 'r') as file:
        lines = file.read().splitlines()

    chosen_url = random.choice(lines)

    urls = [(chosen_url, i) for i in range(n-1)] + [(hotdog_url, unique_game_id)]

    random.shuffle(urls)

    shortened_urls = [create_short_link(url, unique_id) for url, unique_id in urls]

    with open(output_file, 'w') as file:
        for i, url in enumerate(shortened_urls, start=1):
            if url:
                file.write(f"{i}  {url}\n")
    
    print("Roles are ready.")

if __name__ == "__main__":
    input_file = 'input.txt' 
    output_file = 'output.txt'
    player_count = 5 
    main(input_file, output_file, player_count)

