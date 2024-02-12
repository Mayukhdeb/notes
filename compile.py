from papyrus.home import PapyrusHome, Post
import re
import os

def extract_last_component(directory_path):
    # Get the last component of the path
    last_component = os.path.basename(os.path.normpath(directory_path))
    
    return last_component


def extract_metadata(markdown_filename):
    metadata = {}
    
    with open(markdown_filename, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Extracting information within the +++ zone using regex
        match = re.search(r'\+\+\+\s*(.*?)\s*\+\+\+', content, re.DOTALL)
        
        if match:
            metadata_text = match.group(1)
            
            # Parsing metadata key-value pairs
            metadata_lines = metadata_text.split('\n')
            for line in metadata_lines:
                if '=' in line:
                    key, value = map(str.strip, line.split('=', 1))
                    metadata[key.lower()] = eval(value)
                    if key=="title":
                        break
    
    return metadata

def get_filenames_in_a_folder(folder: str):
    """
    returns the list of paths to all the files in a given folder
    """
    
    if folder[-1] == '/':
        folder = folder[:-1]
        
    files =  os.listdir(folder)
    files = [f'{folder}/' + x for x in files]
    return files

def generate_slugs_and_titles_from_post_names(filenames: list):
    filenames.sort()
    filenames.reverse()
    posts = []
    for f in filenames:
        metadata = extract_metadata(f)
        title = metadata["title"]
        slug = extract_last_component(f)

        posts.append(
            Post(
                filename=f,
                slug=slug,
                title=title
            )
        )

    return posts

posts = generate_slugs_and_titles_from_post_names(
    filenames=get_filenames_in_a_folder("content/post")
)
home = PapyrusHome(
    title="Notes",
    body_markdown_filename="home.md",
    posts_folder="posts",
    posts=posts
)

home.compile(output_html_filename="index.html")