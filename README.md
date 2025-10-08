# UIB AI 2025

Repository ini berisi tugas-tugas mata kuliah Artificial Intelligence.

## Struktur Repository

Repository ini menggunakan sistem **branch** di mana setiap branch bersesuaian dengan minggu/tugas tertentu:

- `main` - Branch utama (Tugas 1)
- `tugas-2` - Tugas 2: Fuzzy Logic

## Tugas 2: Sistem Pengatur Kecepatan Kipas AC dengan Fuzzy Logic

Branch ini berisi implementasi sistem kontrol fuzzy logic untuk mengatur kecepatan kipas AC otomatis berdasarkan suhu dan kelembaban ruangan.

### Deskripsi

Sistem ini menggunakan fuzzy logic untuk menentukan kecepatan kipas AC yang optimal berdasarkan:
- **Input 1**: Suhu ruangan (16-40°C)
- **Input 2**: Kelembaban (20-100%)
- **Output**: Kecepatan kipas (0-100%)

### File

- `fuzzy.ipynb` - Jupyter notebook yang berisi implementasi lengkap sistem fuzzy logic
- `ac_dataset.csv` - Dataset untuk testing sistem
- `requirements.txt` - Daftar dependencies yang diperlukan

### Instalasi

1. Pastikan Python 3.13+ terinstal
2. Install dependencies:
```bash
uv pip install -r requirements.txt
```

Atau dengan pip biasa:
```bash
pip install -r requirements.txt
```

3. Install ipykernel untuk menjalankan notebook:
```bash
uv pip install ipykernel
```

### Menjalankan

Buka `fuzzy.ipynb` di Jupyter Notebook atau VS Code, lalu jalankan semua cell secara berurutan.

### Fitur

- Definisi membership functions untuk suhu, kelembaban, dan kecepatan kipas
- 12 fuzzy rules untuk pengambilan keputusan
- Visualisasi membership functions
- Testing dengan dataset
- Perbandingan hasil prediksi vs actual
- Visualisasi 3D surface plot
- Manual testing dengan berbagai skenario

## Cara Mengakses Tugas

Untuk melihat tugas tertentu, pindah ke branch yang sesuai:

```bash
git checkout tugas-2
```

Atau lihat langsung di GitHub dengan memilih branch yang diinginkan.
