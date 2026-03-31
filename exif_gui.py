import tkinter as tk
from tkinter import filedialog, scrolledtext
import subprocess

def analyze_image():
    filepath = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.tiff")]
    )
    
    if filepath:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, f"Analyzing: {filepath}\n{'-'*50}\n")
        
        try:
            result = subprocess.run(['exiftool', filepath], capture_output=True, text=True)
            
            text_area.insert(tk.END, result.stdout)
        except Exception as e:
            text_area.insert(tk.END, f"Error running ExifTool: {e}")


root = tk.Tk()
root.title("ExifTool Analyzer")
root.geometry("600x500")

analyze_btn = tk.Button(root, text="Select Image & Extract Metadata", command=analyze_image, font=("Arial", 14))
analyze_btn.pack(pady=20)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25, font=("Courier", 12))
text_area.pack(padx=20, pady=10)

root.mainloop()