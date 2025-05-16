import asyncio
import time
import concurrent.futures # ThreadPoolExecutor için

def senkron_agir_islem(sure, islem_adi):
    """
    Engellenen (blocking) bir G/Ç veya CPU yoğun işlemi simüle eder.
    Bu fonksiyon 'async def' DEĞİLDİR.
    """
    print(f"[Thread] '{islem_adi}' başlıyor, {sure} saniye sürecek...")
    time.sleep(sure) # Engellenen bir işlemi simüle et (örneğin, dosya okuma, senkron ağ isteği)
    sonuc = f"'{islem_adi}' tamamlandı."
    print(f"[Thread] {sonuc}")
    return sonuc

async def ana_gorev():
    """Ana asenkron görevimiz."""
    loop = asyncio.get_running_loop()

    print("[Async] Ana görev başladı.")

    # ThreadPoolExecutor oluştur (varsayılan olarak CPU sayısına göre thread sayısı ayarlar)
    # None verilirse varsayılan executor kullanılır.
    # Daha fazla kontrol için kendi executor'ınızı oluşturabilirsiniz:
    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

    print("[Async] 'senkron_agir_islem_1' bir thread'de çalıştırılacak...")
    # loop.run_in_executor(executor, engellenen_fonksiyon, arg1, arg2, ...)
    # İlk argüman None ise varsayılan thread pool executor kullanılır.
    gorev1_sonuc_future = loop.run_in_executor(
        None,  # Varsayılan thread pool executor'ı kullan
        senkron_agir_islem, # Çalıştırılacak engellenen fonksiyon
        2,  # senkron_agir_islem için ilk argüman (sure)
        "Senkron İşlem 1" # senkron_agir_islem için ikinci argüman (islem_adi)
    )

    print("[Async] 'senkron_agir_islem_2' bir thread'de çalıştırılacak...")
    gorev2_sonuc_future = loop.run_in_executor(
        None,
        senkron_agir_islem,
        3,
        "Senkron İşlem 2"
    )


    # Bu arada başka asenkron işler yapabiliriz
    print("[Async] Diğer asenkron işler yapılıyor...")
    await asyncio.sleep(0.5) # Başka bir 'await'
    print("[Async] Diğer asenkron işler tamamlandı.")

    # Thread'lerdeki işlemlerin bitmesini bekle ve sonuçlarını al
    # Bir Future nesnesi döndüğü için await ile sonucunu bekleyebiliriz.
    sonuc1 = await gorev1_sonuc_future
    print(f"[Async] Thread'den dönen sonuç 1: {sonuc1}")

    sonuc2 = await gorev2_sonuc_future
    print(f"[Async] Thread'den dönen sonuç 2: {sonuc2}")

    print("[Async] Ana görev bitti.")

if __name__ == "__main__":
    print("Program başlıyor...")
    asyncio.run(ana_gorev())
    print("Program bitti.")
