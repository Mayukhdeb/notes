def get_pandoc_command(
    markdown_filename: str,
    output_html_filename: str,
    style_css_filename: str,
    title: str,
):
    command = f"pandoc --standalone {markdown_filename} -o {output_html_filename} --css={style_css_filename} --metadata title='{title}'"
    return command