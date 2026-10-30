
# Audio NurHarian - Sudah ada placeholder + TTS

## Status Sekarang:
- File mp3 placeholder sudah ada (1 detik silent) biar player tidak error 404
- Web sudah bisa bunyi pakai TTS browser (tombol 🔊 Baca Arab)

## Untuk Audio Asli (Opsi 2):
Jalankan di laptop kamu:

```bash
pip install gTTS requests
python download_real_audio.py
```

Atau download manual:
- Ayat Kursi: https://everyayah.com/data/Alafasy_128kbps/002255.mp3 -> rename jadi d2.mp3
- Al-Mulk: https://everyayah.com/data/Alafasy_128kbps/067001.mp3 -> d6.mp3
- 7 Kalimat & 5 Tergesa: generate di https://ttsmp3.com (pilih Arabic - Salma, paste teks Arab)

Lalu upload semua mp3 ke folder audio/ di repo https://github.com/ayamkurin000-dot/amalan-harian
