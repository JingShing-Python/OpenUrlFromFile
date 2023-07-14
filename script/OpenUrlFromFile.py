import webbrowser

def open_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                if url.startswith('http://') or url.startswith('https://'):
                    webbrowser.open(url)
                else:
                    print(f"not an active url: {url}")
    except FileNotFoundError:
        print("can't find the file")

if __name__ == "__main__":
    file_path = input("Please enter file path: ")
    open_urls_from_file(file_path)
