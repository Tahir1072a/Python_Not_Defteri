import multiprocessing
import time

print("--CPU yoğun işlem---")
big_number = 20_000_000
processes = []

def cpu_intensive_processing_2(number):
    process_name = multiprocessing.current_process().name
    print(f"{process_name}: CPU yoğun işlem başlatılıyor. {number}...")
    sonuc = 0
    for i in range(number):
        sonuc += i
    print(f"{process_name}: CPU yoğun işlem bitti. Sonuc: {sonuc}")

# Buraya sadece main process giriyor.
if __name__ == "__main__":
    print(multiprocessing.current_process().name)
    start_time_mp = time.time()

    for i in range(2):
        process = multiprocessing.Process(target=cpu_intensive_processing_2, args=(big_number,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time_mp = time.time()

    print(f"CPU Yoğun işlem ({2} süreç ile) toplam süre: {end_time_mp - start_time_mp:.2f} saniye")

    print("\n--- Tek Süreçte Sıralı Çalıştırma Karşılaştırması ---")
    start_time_single = time.time()

    for i in range(2):
        cpu_intensive_processing_2(big_number)

    end_time_single = time.time()

    print(f"CPU Yoğun işlem (tek süreç, sıralı, 2 kez) toplam süre: {end_time_single - start_time_single:.2f} saniye")