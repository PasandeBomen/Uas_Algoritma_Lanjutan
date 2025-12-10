def bubble_sort(arr):
    # Mengimplementasikan Algoritma Bubble Sort.
    # Mengurutkan array dari kecil ke besar (ascending).

    n = len(arr)
    print("... Proses Bubble Sort ...")
    print(f"Array awal: {arr}")

    # Loop utama untuk setiap elemen
    for i in range(n - 1):
        # Flag untuk optimasi, jika tidak ada pertukaran (swap)
        # dalam satu iterasi luar, maka array sudah terurut.
        swapped = False

        # Loop untuk membandingkan elemen berpasangan
        # n-i-1 karena i elemen terbesar sudah berada di posisi akhir
        for j in range(0, n - i - 1):

            # Bandingkan elemen saat ini dengan elemen berikutnya
            if arr[j] > arr[j + 1]:
                # Lakukan pertukaran (swap)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Tampilkan hasil iterasi (opsional)
        print(f"Iterasi ke-{i+1}: {arr}")

        # Jika tidak ada pertukaran, hentikan loop
        if not swapped:
            break

    print("... Proses Selesai ...")
    return arr

# data yang akan diurutkan sesuai soal
# data_list = [45, 19, 5, 62, 13, 70, 80, 10, 17, 9]

# Contoh penggunaan:
# data_awal = [45, 19, 5, 62, 13]
# hasil_sort = bubble_sort(data_awal)
# print(f"Array akhir: {hasil_sort}")