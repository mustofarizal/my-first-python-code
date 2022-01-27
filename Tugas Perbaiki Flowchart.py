"""
Tugas Perbaiki Flowchart
"""
print('Ibu berkata, "Beli 1 botol susu')
print('Budi menjawab, "OK"')
print('Maka Budi pergi ke toko')
susu = input('Budi sampai di toko dan bertanya, "Apakah ada susu?"')
if susu == "ada":
    print('Uang cukup untuk membeli susu')
    telur = input('Apakah ada telur?')
    if telur == "ada":
        print('Budi membeli satu botol susu')
    else:
        print('Bumi membeli 6 botol susu')
print('Budi pulang ke rumah')
print('Budi memberikan hasil belanja ke Ibu')