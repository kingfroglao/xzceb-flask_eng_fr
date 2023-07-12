"""
This is a module that translates English text to French. It uses the `MyMemoryTranslator` 
for the translation.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translate text from english to french.
    """
    word = MyMemoryTranslator(source='en-AU', target='fr-FR')
    french_text = word.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translates the french language into English.
    """
    word = MyMemoryTranslator(source='fr-FR', target='en-AU')
    english_text = word.translate(french_text)
    return english_text
