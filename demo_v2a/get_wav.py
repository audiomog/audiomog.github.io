import os
import subprocess

input_dir = r"C:\Users\Dell\Desktop\AudioMoG.github.io\demo_v2a\Video"
output_dir = r"C:\Users\Dell\Desktop\AudioMoG.github.io\demo_v2a\Video_wav"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(".mp4"):
        input_path = os.path.join(input_dir, filename)
        
        # 保持文件名一致，只改后缀
        output_filename = os.path.splitext(filename)[0] + ".wav"
        output_path = os.path.join(output_dir, output_filename)
        
        command = [
            "ffmpeg",
            "-i", input_path,
            "-vn",                # 不要视频
            "-acodec", "pcm_s16le",
            "-ar", "16000",       # 采样率
            "-ac", "2",           # 声道
            output_path
        ]
        
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("全部转换完成！")