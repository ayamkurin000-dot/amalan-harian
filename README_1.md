# NurHarian — Amalan Harian Standalone

Proyek terpisah dari Al-Quran Digital.

## Struktur Repo Baru
```
nurharian-standalone/
├── index.html          <- file utama, single file, siap deploy ke GitHub Pages
├── audio/              <- taruh file mp3 dzikir di sini, nama: k7.mp3, k5.mp3, d1.mp3 dll
├── README.md
└── struktur_amalan_web.json (optional database)
```

## Cara Deploy ke Repo Baru
1. Buat repo baru di GitHub, misal: `nurharian-amalan` atau `nurharian-nixs-21`
2. Upload file `index.html` ini sebagai root
3. Aktifkan GitHub Pages: Settings > Pages > Source: main branch / root
4. Selesai - link akan jadi https://username.github.io/nurharian-amalan/

## Fitur
- Filter by Waktu: Pagi, Siang, Sore, Malam, Sepanjang Waktu, Anytime
- Filter by Tema: Dzikir & Hati, Akhlak & Sosial, Amalan Disegerakan, Perlindungan, Fiqih Ibadah Ringan
- Featured: 7 Kalimat Mulia (Tanbihul Ghafilin Hal.35) & 5 Perkara Boleh Tergesa (Hilyatul Auliya Juz 8 Hal.78)
- Modal detail dengan: teks Arab, transliterasi, arti, dalil, sumber kitab mendalam (juz/hal/no hadits/cetakan), audio player
- Desain mengikuti tema Kemenag, offline ready, font LPMQ + Amiri

## Integrasi dengan Al-Quran Digital
Jika nanti ingin digabung lagi, cukup copy section #amalanPage ke index.html Al-Quran dan tambahkan routing hash #/amalan

## Sumber Kitab
- Tanbihul Ghafilin - Abu Laits As-Samarqandi W.373H Hal.35-36
- Hilyatul Auliya - Abu Nu'aim Juz 8 Hal.78
- Al-Adzkar An-Nawawiyah - Imam Nawawi
- Shahih Bukhari Muslim, Riyadush Shalihin, Ihya Ulumuddin
