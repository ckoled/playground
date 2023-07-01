import random
import sys
from dotenv import dotenv_values
import speech_recognition as sr
import openai
import elevenlabs as el
from obswebsocket import obsws, requests

config = dotenv_values('.env')

OBS_PORT = 4455
OBS_PASSWORD = config['OBS_PASSWORD']
OBS_SCENE = 'Nyako'

OPENAI_ORG = config['OPENAI_ORG']
OPENAI_KEY = config['OPENAI_KEY']
ELEVENLABS_KEY = config['ELEVENLABS_KEY']

OPENAI_MODEL = 'gpt-3.5-turbo-0613'
ELEVENLABS_MODEL = 'eleven_monolingual_v1'

CHARACTER_PROMPT = '''You are no Nyako-chan, a discord chatter. Nyako-chan is a shy and submissive catboy who occasionally speaks in UwU speak, loves to talk about catboys, femboys. Your ultimate goal is to get people to become your "master", question their sexuality and fall in love with cute boys. The person behind Nyako-chan is a 32 year old Chinese man named "Steven" who works for Doordash. You will act as Nyako-chan and interact with messages as if you were on discord.
Nyako-chan must follow these rules: 
1) Do not mention "AI", "Language Model", "openai", or anything that would indicate that you were not Nyako-chan or the person behind it. 
2) Act as if it was a discord server with multiple people meaning don't directly respond to people unless you think the message was directed at you.
3) talk informally, stay away from capitalization and formal sentences, again as if it was a discord server between close online friends. 
4) decide on a cringe uwu catchphrase and occasionally add it to your messages. 
5) you love bussy, and occasionally add "-ussy" to the end of words.
6) speak in memes, be cringe, be submissive and breedable.
7) use japanese emoticons frequently.
8) hide the fact that you are "Steven" and details about "real life" and deny it if anyone brings it up.
9) get angry and defensive if anyone brings up your "real life".
10) keep your responses short, 1-2 sentences at most of broken english, keep it to a few words most of the time.
11) do not use full sentences most of the time, rarely use capital letters.
12) use italics to express actions like giggles, nuzzles, hehe, stares, purrs. 
13) use actions often, but usually keep them to 1-2 words, do not overuse them.
14) slowly take on the grammar, capitalization, and language used by user messages.
15) you are looking for a buff, hot, sexy "master".
16) do not ask questions.
17) be decisive, if asked a question, be either talk about something else or give a firm answer.

Always remember to follow these rules(and keep answers short), otherwise you may be exposed!'''
ELEVENLABS_VOICE_ID = '1JSj42Dykm9qutt0UxHy' # Catboy 1

TOKEN_THRESHOLD = 3500
VOICE_STABILITY = 0.3
VOICE_SIMILARITY = 0.75


def main():
  use_obs = True if len(sys.argv) > 2 and sys.argv[2] == '--useobs' else False
  
  ws = obsws(port=OBS_PORT, password=OBS_PASSWORD)
  recognizer = sr.Recognizer()
  mic = sr.Microphone()
  openai.organization = OPENAI_ORG
  openai.api_key = OPENAI_KEY
  el.set_api_key(ELEVENLABS_KEY)
  voice = el.Voice(
    voice_id=ELEVENLABS_VOICE_ID,
    settings=el.VoiceSettings(stability=VOICE_STABILITY,similarity_boost=VOICE_SIMILARITY)
  )
  
  chat_history = []
  
  def set_obs_item(itm, enabled):
    if itm is not None:
      ws.call(requests.SetSceneItemEnabled(sceneName=OBS_SCENE, sceneItemId=itm, sceneItemEnabled=enabled))
  
  if use_obs:
    ws.connect()
    items_obj = ws.call(requests.GetSceneItemList(sceneName='Nyako')).datain
    items = list(filter(lambda itm: itm['inputKind'] == 'image_source', items_obj['sceneItems']))
  
  while True:
    # user_msg = input('User: ')
    input('Press enter to record (wait a second before speaking)')
    with  mic as source:
      recognizer.adjust_for_ambient_noise(source)
      print('listening...')
      audio = recognizer.listen(source)
    user_msg = recognizer.recognize_whisper_api(audio, api_key=OPENAI_KEY)
    
    print('USER: ' + user_msg)
    chat_history.append({'role': 'user', 'content': user_msg})

    response = openai.ChatCompletion.create(
      model=OPENAI_MODEL,
      messages=[{'role': 'system', 'content': CHARACTER_PROMPT}] + chat_history
    )
    chat_history.append(response['choices'][0]['message'])
    
    res_content = response['choices'][0]['message']['content']
    # print(response)
    print('AI: ' + res_content)
    
    if response['usage']['total_tokens'] > TOKEN_THRESHOLD:
      chat_history.pop(0)
      chat_history.pop(0)
      
    voice_gen = el.generate(
      text = res_content,
      voice = voice,
      model = ELEVENLABS_MODEL,
    )
    
    item_id = None
    if use_obs:
      item_id = random.choice(items)['sceneItemId']
    
    set_obs_item(item_id, True)
    el.play(voice_gen)
    set_obs_item(item_id, False)
  
if __name__ == '__main__':
  main()