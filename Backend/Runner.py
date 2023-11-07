import threading
import subprocess


def run_script(script_name):
    subprocess.run(["python", script_name])


thread1 = threading.Thread(target=run_script, args=("LLaMA-2-7B-ctranformers.py",))
thread2 = threading.Thread(target=run_script, args=("LLaMA-7B-ctranformers.py",))
thread3 = threading.Thread(target=run_script, args=("LLaMA-7B-Chat.py",))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
