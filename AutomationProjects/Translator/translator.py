from googletrans import Translator

translator = Translator()
translation = translator.translate("Hello, how are you? I'm fine, thanks.", dest='it')

print(translation.text)
