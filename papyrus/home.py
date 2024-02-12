import os
from uuid import uuid4
from typing import List
from .pandoc import get_pandoc_command

class Post:
    def __init__(self, filename: str, slug: str, title: str):
        self.filename = filename
        self.slug = slug
        self.title = title

    def compile(self, output_html_filename: str, style_css_filename: str):
        command = get_pandoc_command(
            markdown_filename=self.filename,
            style_css_filename=style_css_filename,
            output_html_filename=output_html_filename,
            title=self.title,
        )
        os.system(command=command)

    def __repr__(self):
        return f'Post(filename="{self.filename}", slug="{self.slug}", title="{self.title}")'

class PapyrusHome:
    def __init__(
        self,
        title: str,
        body_markdown_filename: str,
        posts: List[Post],
        list_of_posts_name="Posts",
        cache_dir: str = ".papyrus",
        base_url: str = "posts",
        posts_folder: str = "posts",
    ) -> None:
        assert os.path.exists(body_markdown_filename), f"Invalid body_markdown_filename: {body_markdown_filename}"
        self.title = title
        self.body_markdown_filename = body_markdown_filename
        self.posts = posts
        self.validate_posts()
        self.style_css_filename = "style.css"
        self.cache_dir = cache_dir
        self.base_url = base_url
        self.posts_folder = posts_folder

        if not os.path.exists(self.cache_dir):
            os.system(f"mkdir -p {self.cache_dir}")

        self.markdown_filename = os.path.join(self.cache_dir, f"{uuid4()}.md")
        os.system(f"cp {self.body_markdown_filename} {self.markdown_filename}")

        # Add a markdown list at the bottom of the Markdown file
        with open(self.markdown_filename, "a") as markdown_file:
            markdown_file.write(f"\n## {list_of_posts_name}\n")
            for post in self.posts:
                markdown_file.write(
                    f"- [{post.title}]({self.base_url}/{post.slug}.html)\n"
                )

    def validate_posts(self):
        seen_slugs = set()
        for post in self.posts:
            assert os.path.exists(post.filename), f"File not found: {post.filename}"
            assert post.filename.endswith(
                f".md"
            ), f"Expected the filename to end with `.md` but got filename: {post.filename}"
            # Check for repeating slugs
            assert post.slug not in seen_slugs, f"Duplicate slug found: {post.slug}"
            seen_slugs.add(post.slug)

    def compile(self, output_html_filename: str):
        command = get_pandoc_command(
            markdown_filename=self.markdown_filename,
            output_html_filename=output_html_filename,
            style_css_filename=self.style_css_filename,
            title=self.title,
        )
        os.system(command=command)
        os.system(f"rm {self.markdown_filename}")
        self.compile_posts()
        print("Done!")

    def compile_posts(self):
        assert os.path.exists(
            self.posts_folder
        ), f"Invalid output_folder: {self.posts_folder}"

        for post in self.posts:
            post.compile(
                output_html_filename=os.path.join(
                    self.posts_folder, f"{post.slug}.html"
                ),
                style_css_filename=os.path.join("../", self.style_css_filename),
            )
        print(f"Compiled {len(self.posts)} pages")
