from gtts import gTTS
import os

# will read the file to convert into audio
text_File = open("text.txt", "r")
myText = text_File.read().replace("\n", " ")
# line ending er jaygay jate shesh na vabe instead break nibe bolar time a


language = 'en'

# slow means audio will played slow
output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

text_File.close()

os.system("start output.mp3")
