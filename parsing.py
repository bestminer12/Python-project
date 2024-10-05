import tkinter as tk

def parse_text():
    # 첫 번째 텍스트 박스의 내용을 가져옴
    input_text = input_textbox.get("1.0", tk.END).strip()

    # 입력받은 텍스트를 쉼표로 파싱
    prefix = "<li>"
    suffix = "</li>"

    parsed_values = input_text.splitlines()
    modified_lines = [f"{prefix}{line}{suffix}" for line in parsed_values]
    modified_lines = "\n".join(modified_lines)
    result = "<ul>\n" + modified_lines + "\n</ul>"

    # 출력 텍스트 박스 초기화
    output_textbox.delete("1.0", tk.END)

    # 각 파싱된 값을 새로운 줄에 출력

    output_textbox.insert(tk.END, result)

# 메인 윈도우 생성
root = tk.Tk()
root.title("Text Input and Parsing")
root.geometry("800x600")

# 첫 번째 텍스트 박스 (입력용)
input_label = tk.Label(root, text="Input Text (comma separated):")
input_label.pack(pady=5)
input_textbox = tk.Text(root, height=10, width=80)
input_textbox.pack(pady=10)

new_prefix = "<li>"
new_suffix = "</li>"
# 버튼 생성
parse_button = tk.Button(root, text="Parse Text", command=parse_text)
parse_button.pack(pady=10)

# 두 번째 텍스트 박스 (출력용)
output_label = tk.Label(root, text="Parsed Output:")
output_label.pack(pady=5)
output_textbox = tk.Text(root, height=10, width=80)
output_textbox.pack(pady=10)

root.mainloop()