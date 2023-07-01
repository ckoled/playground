from obswebsocket import obsws, requests
import random
import time

# Connect to OBS
ws = obsws(port=4455, password='obstest')
ws.connect()

items = ws.call(requests.GetSceneItemList(sceneName='Nyako'))
# print(items) # 11
for item in items.datain['sceneItems']:
    print(item)
    
item = random.choice(items.datain['sceneItems'])
ws.call(requests.SetSceneItemEnabled(sceneName='Nyako', sceneItemId=item['sceneItemId'], sceneItemEnabled=True))
time.sleep(3)
ws.call(requests.SetSceneItemEnabled(sceneName='Nyako', sceneItemId=item['sceneItemId'], sceneItemEnabled=False))

ws.disconnect()
exit()

import numpy as np

def calculate_audio_volume(input_data):
    # Convert the raw byte audio data to a numpy array
    audio_samples = np.frombuffer(input_data, dtype=np.int16)

    # Calculate the RMS value of the audio samples
    rms = np.sqrt(np.mean(np.square(audio_samples)))

    # You can perform additional scaling or processing as needed
    # For example, you may want to map the RMS value to a desired range

    return 0 if np.isnan(rms) else rms


import pyaudio

# Initialize audio input
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=2048)

# Audio callback function
def process_audio(input_data, frame_count, time_info, status):
    # Analyze audio and update graphic animation based on sound

    # Example: Update a text source named "MyTextSource" with audio volume
    volume = calculate_audio_volume(input_data)
    print(volume)

    # Prepare the properties dictionary
    properties = {"text": f"Volume: {volume}"}

    # Call the SetTextGDIPlusProperties request with the source name and properties
    # ws.call(obswebsocket.requests.SetTextGDIPlusProperties(source_name="MyTextSource", **properties))
    
    ws.call(requests.SetSceneItemTransform(sceneName='Cam', sceneItemId=5, sceneItemTransform={'positionX': volume*2}))
    
    return (input_data, pyaudio.paContinue)


# Start audio input stream
stream.start_stream()

while True:
    # Read audio data from the stream
    input_data = stream.read(2048, exception_on_overflow=False)

    # Process audio and update graphic animation
    process_audio(input_data, 2048, None, None)
