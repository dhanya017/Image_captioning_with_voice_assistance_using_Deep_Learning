from flask import Flask, render_template, url_for, request, redirect
from caption import * 
import warnings
warnings.filterwarnings("ignore")
import gtts
import pyttsx3
#import os
import uuid




app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']

		# print(img)
		# print(img.filename)

		img.save("static/"+img.filename)

	
		caption = caption_this_image("static/"+img.filename)
	
		#def caption_to_voice(caption):
			#sound=pyttsx3.init()
			#ob=gtts.gTTS(caption)
			#return ob.save("w.mp3")
			#sound.say(caption)
			#sound.runAndWait()
			#audio_filename = str(uuid.uuid4()) + ".mp3"  # Generate a unique filename
			#sound = pyttsx3.init()
			#ob = gtts.gTTS(caption)
			#ob.save("sp/" + audio_filename)
    		#return audio_filename
		

		def caption_to_voice(caption):
			audio_filename = str(uuid.uuid4()) + ".mp3"  # Generate a unique filename
			sound = pyttsx3.init()
			ob = gtts.gTTS(caption)
			ob.save("static/" + audio_filename)
			return audio_filename


		
		#caption_to_voice(caption)	
		speech=caption_to_voice(caption)


		
		result_dic = {
			'image' : "static/" + img.filename,
			'description' : caption,
			'audio_filename': speech
		}
		
	return render_template('index.html', results = result_dic)



if __name__ == '__main__':
	app.run(debug = True)