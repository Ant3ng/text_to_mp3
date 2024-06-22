import os
import sys
from gtts import gTTS
from tqdm import tqdm

def is_text_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.read()
        return True
    except Exception as e:
        return False

def text_to_mp3(input_filename, output_folder):
    print(input_filename)
    if not is_text_file(input_filename):
        print(f"{input_filename} はテキストファイルではありません。")
        return

    tts = gTTS(text=open(input_filename, "r", encoding="utf-8").read(), lang='ja')

    # 出力ファイルの拡張子を取得
    base_name, _ = os.path.splitext(os.path.basename(input_filename))
    
    # 出力ファイルのパスを作成
    output_filename = os.path.join(output_folder, base_name + ".mp3")

    tts.save(output_filename)

def convert_folder_to_mp3(input_folder, output_folder="output_folder"):
    if not os.path.isdir(input_folder):
        print(f"{input_folder} が見つかりません。存在するフォルダ名を指定してください。")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in tqdm(os.listdir(input_folder), desc="Converting"):
        input_path = os.path.join(input_folder, file_name)
        text_to_mp3(input_path, output_folder)

def main():
    if len(sys.argv) < 2:
        print("使用法: python3 スクリプト名.py フォルダ名 [出力フォルダ名]")
        sys.exit(1)

    input_folder = sys.argv[1]

    # コマンドライン引数で出力フォルダが指定されているか確認し、指定がなければデフォルトの "output_folder" を使用
    if len(sys.argv) >= 3:
        output_folder = sys.argv[2]
    else:
        output_folder = "output_folder"

    convert_folder_to_mp3(input_folder, output_folder)

    print("変換が完了しました.")

if __name__ == "__main__":
    main()

