import time
from playsound import playsound

def focus_timer(duration):
    print("开始专注工作！加油！")
    time.sleep(duration)  # 按指定时间段延时
    playsound('path/to/alert_sound.mp3')  # 播放提醒音频
    print("时间到！结束专注。")

# 设置专注时长（以秒为单位）
focus_duration = 1800  # 30分钟

focus_timer(focus_duration)
