""""
Aplikasi pendeteksi gempa terkini
Modularisasi Dengan Function
"""


def ekstrasksi_data():

    """
    Tanggal : 24 Agustus 2021
    Waktu : 12:06:62 WIB
    Magnitudo : 4.0
    Kedalaman : 40 Km
    Lokasi : LS=1.48 BT=134.01
    Pusat Gempa : Pusat gempa berada di darat 19km barat laut ransiki
    Jangkauan :dirasakan (skala MMI) : II-III monokwari , II-III ransiki
    """
    hasil = dict()
    hasil ['tanggal'] = '24 Agustus 2021'
    hasil ['waktu'] = '12:06:62 WIB'
    hasil ['magnitudo'] = 4.0
    hasil ['kedalaman'] = 40
    hasil ['lokasi'] = {'ls' : 1.48 , 'bt' : 134.01}
    hasil ['pusat'] = 'Pusat gempa berada di darat 19km barat laut ransiki'
    hasil ['jangkauan'] = 'dirasakan (skala MMI) : II-III monokwari , II-III ransiki'


    return hasil

def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : LS= {result['lokasi']['ls']} , BT ={result['lokasi']['ls']}")
    print(f"Pusat : {result['pusat']}")
    print(f"Jangkauan : {result['jangkauan']}")



if __name__ =='__main__':
    print('Aplikasi Utama')
    result = ekstrasksi_data()
    tampilkan_data(result)

