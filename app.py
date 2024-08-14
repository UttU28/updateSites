import os, subprocess

index_html_path = 'index.html'
def update_redirect_url(new_url):
    with open(index_html_path, 'r') as file:
        content = file.read()
    search_string = 'window.location.href = \''
    replace_string = f'window.location.href = \'{new_url}\';'
    
    if search_string in content:
        content = content.replace(content.split(search_string)[1].split('\'')[0], new_url)
    else:
        content = content.replace('<body>', '<body>\n<script type="text/javascript">\n' +
                                  f'window.location.href = \'{new_url}\';\n' +
                                  '</script>')
    
    with open(index_html_path, 'w') as file:
        file.write(content)

def run_git_commands():
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Updated redirect URL JSK'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Changes committed and pushed to the repository.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing Git commands: {e}")

def main():
    new_url = input("Enter the new URL for redirection: ")
    if not new_url.startswith('http://') and not new_url.startswith('https://'):
        print("Invalid URL. Make sure it starts with 'http://' or 'https://'.")
        return
    update_redirect_url(new_url)
    print(f"Redirect URL updated to: {new_url}")
    run_git_commands()

if __name__ == "__main__":
    main()
