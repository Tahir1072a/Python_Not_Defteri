import functools

def tekrarla(kac_kere):
    """
    Bu bir dekoratör fabrikasıdır.
    Dekore edilen fonksiyonu 'kac_kere' kadar çalıştıracak bir dekoratör döndürür.
    """
    print(f"Tekrarla dekoratör fabrikası {kac_kere} kere için çağrıldı.")
    def gercek_dekorator(func):
        print(f"  '{func.__name__}' fonksiyonu {kac_kere} kere tekrarlama ile dekore ediliyor.")
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"    '{func.__name__}' {kac_kere} kere çalıştırılacak:")
            son_sonuc = None
            for i in range(kac_kere):
                print(f"      {i+1}. çalıştırma:")
                son_sonuc = func(*args, **kwargs)
            return son_sonuc # En son çalışmanın sonucunu döndür
        return wrapper
    return gercek_dekorator


@tekrarla(kac_kere=3) # Dekoratöre argüman veriyoruz
def selam_ver(isim):
    print(f"      Merhaba, {isim}!")
    return f"Selam {isim}"

sonuc = selam_ver("Dünya")
print(f"\nSonuç: {sonuc}")