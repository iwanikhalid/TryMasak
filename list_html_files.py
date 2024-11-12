import os

def list_html_files(base_path):
    html_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".html") or file.endswith(".htm"):
                # Get the relative path for the file
                relative_path = os.path.relpath(os.path.join(root, file), start=".")
                html_files.append(relative_path)
    return sorted(html_files)  # Sort the files alphabetically

def generate_index_html(html_files_by_dir):
    content = "<html><body>\n"
    
    for dir_name, files in html_files_by_dir.items():
        content += f"<h3>{dir_name.capitalize()}</h3>\n<ul>\n"
        for file_path in files:
            content += f'<li><a href="{file_path}">{file_path}</a></li>\n'
        content += "</ul>\n"
    
    content += "</body></html>"
    return content

if __name__ == "__main__":
    # Specify base directories
    base_dirs = {"Wireframe": "./wireframe", "UI": "./ui"}
    html_files_by_dir = {}

    # Collect HTML files by directory
    for dir_name, base_dir in base_dirs.items():
        html_files_by_dir[dir_name] = list_html_files(base_dir)

    # Generate index.html content
    index_html_content = generate_index_html(html_files_by_dir)

    # Write to index.html
    with open("index.html", "w") as f:
        f.write(index_html_content)

    print("index.html has been created with links to all .html and .htm files.")
