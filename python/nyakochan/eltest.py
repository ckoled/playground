import elevenlabs as el
import nyako
import os

el.set_api_key(nyako.ELEVENLABS_KEY)

# audio_stream = el.generate(
#   text = 'This is a... streaming voice!!',
#   voice = nyako.ELEVENLABS_VOICE_ID,
#   model = nyako.ELEVENLABS_MODEL,
# )

# el.save(audio_stream, 'temp.wav')
print('saved')
os.system('ffplay temp.wav')
print('done')