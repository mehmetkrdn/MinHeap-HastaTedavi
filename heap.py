import heapq

def veri_ekle():
    while True:
        print("Yapmak istediğiniz işlemi seçin:")
        print("1- Yeni veri ekle")
        print("2- Yapıyı göster")
        print("3- Tedavi simülasyonu")
        print("4- Çıkış")
        secim = input("\nSeçiniz 1-2-3-4: ")

        if secim == '1':
            #veri alırız
            id = int(input("ID: "))
            oncelik = int(input("Öncelik no: "))
            sure = int(input("Tedavi süresi: "))
            heapq.heappush(min_heap, (oncelik, id, sure))
            print("\nVeri eklendi ve min heap düzenlendi.")
            print("Güncel min heap sıralaması:")
            for eleman in sorted(min_heap):
                print(eleman)

        elif secim == '2':
            # Mevcut min heap yapısını gösterir
            print("\nGüncel min heap sıralaması:")
            for datas in heapq.nsmallest(len(min_heap), min_heap):
                print(datas)

        elif secim == '3':
            # Tedavi simülasyonu
            print("\nTedavi Simülasyonu Başlıyor...")
            toplam_tedavi_suresi = 420  # Gün sonunda toplam 7 saatlik tedavi süresi
            tedavi_edilenler = []
            tedavi_edilemeyenler = []

            # Min heap'i kullanarak tedavi süresi
            while min_heap:
                oncelik, id, sure = heapq.heappop(min_heap)
                if sure <= toplam_tedavi_suresi:
                    tedavi_edilenler.append((oncelik, id, sure))
                    toplam_tedavi_suresi -= sure
                else:
                    tedavi_edilemeyenler.append((oncelik, id, sure))

            #tedavi edilen ve edilemeyenleri yazdır
            print("\nTedavi Edilen Hastalar:")
            for hasta in tedavi_edilenler:
                print(hasta)

            print("\nTedavi Edilemeyen Hastalar:")
            for hasta in tedavi_edilemeyenler:
                print(hasta)

            # Tedavi edilemeyen hastalar tekrar min heape eklenir ertesi gün için
            for hasta in tedavi_edilemeyenler:
                heapq.heappush(min_heap, hasta)

        elif secim == '4':
            break

# başlangıç verileri
veriler = [
    (101, 5, 30), (102, 3, 40), (103, 8, 20), (104, 1, 60), (105, 7, 15),
    (106, 2, 50), (107, 4, 45), (108, 6, 25), (109, 3, 35), (110, 2, 30),
    (111, 8, 10)
]
min_heap = []

# başlangıç verilerini min heape eklenir
for veri in veriler:
    heapq.heappush(min_heap, (veri[1], veri[0], veri[2]))#önce öncelik sırası eklenir.

print("Min heap sıralaması:")
for eleman in sorted(min_heap):
    print(eleman)

print("Dinamik veri ekleme ve simülasyon")
karar=input("Veri eklensin mi: ")
if karar=='evet':
    veri_ekle()
elif karar=='hayır':
    print("Program bitti")
