import time
import google.generativeai as genai
import pyperclip
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

# Configure the Gemini API client
genai.configure(api_key="YOUR GEMINI API KEY HERE")

def show_popup(response):
    app = QApplication([])

    popup = QWidget()
    popup.setWindowTitle("Ansir")

    popup.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

    popup.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    popup.setWindowOpacity(0.9)

    label = QLabel(response, popup)
    label.setStyleSheet("""
        QLabel {
            color: white;
            background-color: black;
            padding: 10px;
            border-radius: 10px;
            font-size: 14px;
            word-wrap: break-word;
            max-width: 350px;
        }
    """)
    label.adjustSize()
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    screen_geometry = app.primaryScreen().geometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()
    label_width = label.width()
    label_height = label.height()

    margin = 50
    popup.move((screen_width - label_width) // 2, screen_height - label_height - margin)

    popup.show()

    QTimer.singleShot(4000, popup.close)
    app.exec()

def send_to_gemini(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Customize the prompt for getting answer from gemini
        response = model.generate_content(
            'In this question, go through the question very carefully and give the correct answer from the options given. Analyze the following multiple-choice question and determine the correct answer. Provide only the letter (A, B, C, D) corresponding to the correct option, followed by the text of the correct answer. Do not include any additional explanation or text. Do use web or internet to get the most accurate and correct answer possible : ' + str(prompt)
        )

        return response.text
    except Exception as e:
        print(f"Error in sending message: {e}")
        return None

def write_to_file(filename, data):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(data + "\n")
        print(f"Data written to {filename} successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    previous_clipboard_content = pyperclip.paste()

    while True:
        current_clipboard_content = pyperclip.paste()

        if current_clipboard_content != previous_clipboard_content:
            print(f"Clipboard changed: {current_clipboard_content}")

            response = send_to_gemini(current_clipboard_content)

            if response:
                print(f"Gemini Response: {response}")
                show_popup(response)

                write_to_file("Ansir.log", "\n\nQuestion:\n" + current_clipboard_content + "\n\nAnswer:\n" + response)

            previous_clipboard_content = current_clipboard_content

        time.sleep(1)

if __name__ == "__main__":
    main()
