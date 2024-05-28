import gradio as gr
import os

def fetch(url, name, ext):
    opts = {
        "mp3": "-f \"ba\" -x --audio-format mp3",
        "mp4": "-f \"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best\"",
    }[ext]
    filename = f"{name}.{ext}"
    os.system(f"yt-dlp {opts} {url} -o {filename}")
    return filename

# Create the Gradio interface
interface = gr.Interface(
    fn=fetch, 
    inputs=[
        gr.Textbox(label="Link Address", placeholder="Enter the url here ..."),
        gr.Textbox(label="File name", placeholder="Example: file_name"),
        gr.Dropdown(["mp3", "mp4"], value="mp4", label="File type")
    ],
    outputs=gr.File(label="Download!"),
    description="Download from X, Youtube, Reddit, etc..",
    theme="xiaobaiyuan/theme_brief"
)

# Launch the interface
interface.launch()
