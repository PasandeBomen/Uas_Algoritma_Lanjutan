# UAS_Algoritma_Lanjutan
import collections
import sys

my_stack = collections.deque()

def append_element(element):
    """Menambahkan elemen ke ujung kanan Stack"""
    my_stack.append(element)
    print(f"✅ Elemen '{element}' ditambahkan. Stack saat ini: {list(my_stack)}")

def appendleft_element(element):
    """Menambahkan elemen ke ujung kiri Stack"""
    my_stack.appendleft(element)
    print(f"✅ Elemen '{element}' ditambahkan ke kiri. Stack saat ini: {list(my_stack)}")

def pop_element():
    """Menghapus dan mengembalikan elemen dari ujung kanan Stack"""
    if my_stack:
        element = my_stack.pop()
        print(f"🗑️ Elemen '{element}' dihapus dari kanan. Stack saat ini: {list(my_stack)}")
        return element
    else:
        print("❌ Stack kosong, tidak dapat melakukan 'pop'.")
        return None

def popleft_element():
    """Menghapus dan mengembalikan elemen dari ujung kiri Stack"""
    if my_stack:
        element = my_stack.popleft()
        print(f"🗑️ Elemen '{element}' dihapus dari kiri. Stack saat ini: {list(my_stack)}")
        return element
    else:
        print("❌ Stack kosong, tidak dapat melakukan 'popleft'.")
        return None

def clear_stack():
    """Menghapus semua elemen dari Stack"""
    my_stack.clear()
    print("🧹 Stack telah DIHAPUS. Stack saat ini: []")

def show_menu():
    """Menampilkan menu dan memproses input pengguna"""
    print("\n" + "="*30)
    print("OPERASI STACK")
    print("="*30)
    print("1. Append (Tambah Kanan)")
    print("2. AppendLeft (Tambah Kiri)")
    print("3. Pop (Hapus Kanan)")
    print("4. PopLeft (Hapus Kiri)")
    print("5. Clear (Hapus Semua)")
    print("6. Keluar/Quit")
    print(f"Stack saat ini: {list(my_stack)}")
    print("="*30)

def main_stack():
    """Fungsi utama untuk menjalankan program Stack"""
    initial_data = ["A", "B", "C"]
    my_stack.extend(initial_data)
    print(f"Stack diinisialisasi dengan: {list(my_stack)}")

    while True:
        show_menu()
        choice = input("Pilih operasi (1-6): ").strip()

        if choice == '1':
            item = input("Masukkan elemen untuk di-Append: ").strip()
            if item:
                append_element(item)
        elif choice == '2':
            item = input("Masukkan elemen untuk di-AppendLeft: ").strip()
            if item:
                appendleft_element(item)
        elif choice == '3':
            pop_element()
        elif choice == '4':
            popleft_element()
        elif choice == '5':
            clear_stack()
        elif choice == '6':
            print("👋 Program Stack selesai. Sampai jumpa!")
            sys.exit(0)
        else:
            print("❗ Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_stack()
