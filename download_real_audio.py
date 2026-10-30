
# download_real_audio.py - Jalankan di laptop kamu yang ada internet
# pip install gTTS requests

import os
from gtts import gTTS

audios = {
    "k7": "بسم الله الرحمن الرحيم، الحمد لله، استغفر الله، ان شاء الله، لا حول ولا قوة الا بالله العلي العظيم، انا لله وانا اليه راجعون، لا اله الا الله محمد رسول الله",
    "k5": "اطعام الضيف اذا نزل، وتجهيز الميت اذا مات، وتزويج البكر اذا ادركت، وقضاء الدين اذا وجب، والتوبة من الذنب اذا اذنب",
    "d1": "اللهم انت ربي لا اله الا انت خلقتني وانا عبدك وانا على عهدك ووعدك ما استطعت",
    "d4": "سبحان الله وبحمده سبحان الله العظيم",
}

os.makedirs("audio", exist_ok=True)

for name, text in audios.items():
    tts = gTTS(text=text, lang='ar')
    tts.save(f"audio/{name}.mp3")
    print(f"Saved audio/{name}.mp3")

# Untuk Ayat Kursi & Al-Mulk download dari EveryAyah
import requests

def download_everyayah(surah, ayah, filename):
    # Mishary Rashid Alafasy
    url = f"https://everyayah.com/data/Alafasy_128kbps/{surah:03d}{ayah:03d}.mp3"
    r = requests.get(url)
    if r.status_code == 200:
        open(f"audio/{filename}.mp3","wb").write(r.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed {url}")

# Ayat Kursi = Al-Baqarah 255
download_everyayah(2, 255, "d2")
# Al-Mulk 1-3 sebagai contoh
download_everyayah(67, 1, "d6")

print("Selesai! Upload folder audio ke GitHub repo amalan-harian kamu")
