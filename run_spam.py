import sys
import subprocess
from multiprocessing import Pool

def run_spam(phone_number, spam_count):
    # Chạy script spamv3.py với các tham số
    command = f"python spamv3.py {phone_number} {spam_count}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    phone_number = sys.argv[1]  # Số điện thoại
    spam_count = int(sys.argv[2])  # Số lần spam
    num_threads = int(sys.argv[3])  # Số tiến trình chạy song song

    # Chia số lần spam ra cho các luồng
    count_per_thread = spam_count // num_threads
    pool = Pool(num_threads)

    # Sử dụng multiprocessing để chạy đồng thời
    pool.starmap(run_spam, [(phone_number, count_per_thread) for _ in range(num_threads)])

    pool.close()
    pool.join()
