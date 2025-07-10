import os
import shutil
import re
import requests

def move_jpg_files():
    source = 'source_folder'
    dest = 'destination_folder'
    os.makedirs(dest, exist_ok=True)
    for filename in os.listdir(source):
        if filename.lower().endswith('.jpg'):
            shutil.move(os.path.join(source, filename), os.path.join(dest, filename))
            print(f"Moved: {filename}")

def extract_emails():
    with open('input.txt', 'r') as file:
        content = file.read()
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
    with open('emails.txt', 'w') as file:
        for email in emails:
            file.write(email + '\n')
    print(f"Extracted {len(emails)} emails.")

def scrape_title():
    url = 'https://example.com'
    try:
        response = requests.get(url)
        match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
        if match:
            title = match.group(1)
            with open('title.txt', 'w') as file:
                file.write(title)
            print(f"Page Title: {title}")
        else:
            print("Title not found.")
    except Exception as e:
        print(f"Error fetching URL: {e}")

# Choose which function to run here:
if __name__ == "__main__":
    move_jpg_files()
    extract_emails()
    scrape_title()
