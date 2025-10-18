def hitung_rata_rata(daftar_nilai):
    """Menghitung rata-rata dari list nilai."""
    total = 0
    for nilai in daftar_nilai:
        total += nilai
    
    if daftar_nilai: 
        rata_rata = total / len(daftar_nilai)
        return rata_rata
    else:
        return 0


def tampilkan_status_program(pesan):
    """Menampilkan pesan status program."""
    print("--------------------------------------------------")
    print(f"[STATUS] {pesan}")
    print("--------------------------------------------------")

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.nilai = [] 


    def cek_kelulusan(self):
        """Menentukan status Lulus atau Tidak Lulus (Return Type)."""
        rerata = hitung_rata_rata(self.nilai)
        
        if rerata >= 60:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_hasil(self, nilai_minimal_lulus):
        """Menampilkan laporan lengkap (Non-Return Type)."""
        rerata = hitung_rata_rata(self.nilai)
        status = self.cek_kelulusan() 

        print(f"\n[HASIL PENILAIAN] {self.nama} ({self.nim})")
        print(f"Daftar Nilai: {self.nilai}")
        print(f"Rata-rata Nilai: {rerata:.2f}")

        if status == "LULUS":
            print(f"Selamat! Status: {status} (Rata-rata >= {nilai_minimal_lulus}) ")
        elif rerata >= 50:
            print(f"Status: {status}. Perlu perbaikan.")
        else:
            print(f"Status: {status}. Disarankan mengulang.")


NILAI_MINIMAL_LULUS = 60

tampilkan_status_program("Program Penilaian Dimulai")
siswa_a = Mahasiswa("Jasmine Dzakiya", "21120125140164")
siswa_b = Mahasiswa("Joko", "010203040506")

print("\n--- Input Data ---")
siswa_a.nilai = [90, 95, 93, 96, 97] 
siswa_b.nilai = [40, 55, 60, 35, 50] 


rata_budi = hitung_rata_rata(siswa_a.nilai)
rata_ayu = hitung_rata_rata(siswa_b.nilai)

print(f"Rata-rata Jasmine (Via Function): {rata_budi:.2f}")
print(f"Rata-rata Joko (Via Function): {rata_ayu:.2f}")

siswa_a.tampilkan_hasil(NILAI_MINIMAL_LULUS)
siswa_b.tampilkan_hasil(NILAI_MINIMAL_LULUS)

tampilkan_status_program("Program Selesai")
