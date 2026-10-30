
// NurHarian TTS Fallback - Uses Browser Web Speech API for Arabic
// If mp3 file missing or empty, it will speak Arabic text directly
function speakArabic(text) {
  if (!('speechSynthesis' in window)) {
    alert('Browser tidak support Text-to-Speech');
    return;
  }
  speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = 'ar-SA';
  utter.rate = 0.8;
  utter.pitch = 1;
  // Try to find Arabic voice
  const voices = speechSynthesis.getVoices();
  const arVoice = voices.find(v => v.lang.includes('ar')) || voices[0];
  if (arVoice) utter.voice = arVoice;
  speechSynthesis.speak(utter);
}

function playWithFallback(id, arabText) {
  const audioEl = document.getElementById('aud');
  const src = audioEl ? audioEl.querySelector('source').src : '';
  // If audio file exists and has content, play it, otherwise use TTS
  if (audioEl && audioEl.duration > 0.5) {
    audioEl.play();
  } else {
    speakArabic(arabText);
  }
}
