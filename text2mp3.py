import sys
from gtts import gTTS

def text_to_mp3(input_filename, output_filename="output.mp3"):
    # テキストファイルからテキストを読み込む
    with open(input_filename, "r", encoding="utf-8") as file:
        text = file.read()

    # gTTSオブジェクトを作成
    tts = gTTS(text=text, lang='ja')

    # MP3ファイルとして保存
    tts.save(output_filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用法: python3 スクリプト名.py テキストファイル名 [出力ファイル名]")
        sys.exit(1)

    input_text_filename = sys.argv[1]

    # コマンドライン引数で出力ファイル名が指定されているかを確認し、指定がなければデフォルトの "output.mp3" を使用
    if len(sys.argv) >= 3:
        output_mp3_filename = sys.argv[2]
    else:
        output_mp3_filename = "output.mp3"

    text_to_mp3(input_text_filename, output_mp3_filename)

