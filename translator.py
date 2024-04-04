import cv2
import pytesseract
from google.cloud import translate

def recognize_handwritten_text(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Preprocess the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # Recognize text using Tesseract OCR
    text = pytesseract.image_to_string(thresholded)
    return text

def parse_text(text):
    # Implement your parsing logic here (e.g., split sentences, extract words)
    # For simplicity, you can split the text into sentences based on punctuation marks
    sentences = text.split('.')
    return sentences

def translate_text(text, target_language='es'):# CHANGE LANG HERE, html language codes (eg. en, es, fr, zh)
    project_id = 'ttnlppp'
    # Initialize the Translation API client
    client = translate.TranslationServiceClient()
    # Translate the text to the target language
    response = client.translate_text(
        parent=f'projects/{project_id}',
        contents=[text],
        target_language_code=target_language,
    )
    translated_text = response.translations[0].translated_text
    return translated_text

# Example usage
# image_path = 'handwritten_text.jpg'
# recognized_text = recognize_handwritten_text(image_path)
# parsed_sentences = parse_text(recognized_text)
# for sentence in parsed_sentences:
#     translated_sentence = translate_text(sentence)
#     print(f'Translated Sentence: {translated_sentence}')

def main():
    image_path = 'meditations2.jpg'
    recognized_text = recognize_handwritten_text(image_path)
    parsed_sentences = parse_text(recognized_text)

    print(recognized_text)
    print(parsed_sentences)

    print(pytesseract.get_languages())

    output=''
    for sentence in parsed_sentences:
        translated_sentence = translate_text(sentence)
        #print(f'Translated Sentence: {translated_sentence}')
        #print(translated_sentence, end='')
        output = output+translated_sentence
    print(output)

def runit(image_path):
    recognized_text = recognize_handwritten_text(image_path)
    parsed_sentences = parse_text(recognized_text)

    output=''
    for sentence in parsed_sentences:
        translated_sentence = translate_text(sentence)
        #print(f'Translated Sentence: {translated_sentence}')
        #print(translated_sentence, end='')
        output = output+translated_sentence

    return output
