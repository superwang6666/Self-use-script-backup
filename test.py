import os
import shutil
import re
import time

def process_videos():
    # 获取当前脚本所在目录
    current_dir = os.getcwd()
    
    # 支持的视频文件扩展名
    video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.mp4')
    
    # 定义多个正则表达式模式
    patterns = [
        r'([^.]+)\.(\d{4})\.',              # 匹配 Anora.2024.mp4
        r'(.+?)[\s.](\d{4})\.',             # 匹配 Movie Name.2024.mp4 或 Movie.Name.2024.mp4
        r'(.+?)\.(\d{4})\.(?:BD|HD|WEB-DL)', # 匹配 机器人之梦.2023.BD.1080P.中字.mkv
    ]
    
    # 获取所有视频文件
    video_files = [f for f in os.listdir(current_dir) if f.lower().endswith(video_extensions)]
    total_files = len(video_files)
    
    if total_files == 0:
        print("\n未找到视频文件！")
        input("\n按回车键退出...")
        return
    
    print(f"\n找到 {total_files} 个视频文件，开始处理...\n")
    processed_count = 0
    success_count = 0
    
    for filename in video_files:
        processed_count += 1
        print(f"正在处理 ({processed_count}/{total_files}): {filename}")
        
        # 尝试所有模式进行匹配
        match = None
        for pattern in patterns:
            match = re.search(pattern, filename)
            if match:
                break
        
        if match:
            movie_name = match.group(1).replace('.', ' ').strip()
            year = match.group(2)
            
            # 构建目标文件夹名
            folder_name = f"{movie_name}({year})"
            
            # 确保目标文件夹存在
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            
            # 构建目标路径
            target_path = os.path.join(folder_name, filename)
            
            try:
                # 移动文件
                shutil.move(filename, target_path)
                success_count += 1
                print(f"✓ 成功移动到: {folder_name}\n")
            except Exception as e:
                print(f"✗ 移动失败: {str(e)}\n")
        else:
            print(f"✗ 无法识别文件名格式\n")
    
    # 显示最终处理结果
    print("\n处理完成！")
    print(f"总计文件: {total_files}")
    print(f"成功处理: {success_count}")
    print(f"处理失败: {total_files - success_count}")
    
    input("\n按回车键退出...")

if __name__ == "__main__":
    print("=== 视频文件整理工具 ===")
    print("本程序将自动整理视频文件到对应文件夹")
    print("支持的格式: mp4, mkv, avi, mov, wmv")
    print("=" * 25)
    
    try:
        process_videos()
    except Exception as e:
        print(f"\n程序发生错误: {str(e)}")
        input("\n按回车键退出...")

