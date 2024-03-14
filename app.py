from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator
from PIL import Image
from io import BytesIO
import requests

st.title('Análisis de Sentimiento')
image = Image.open('emoticones.jpg')
st.image(image)
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

def create_image_from_sentiment(text):
  """
  Creates an image based on the sentiment of the given text.

  Args:
    text: The text to analyze.

  Returns:
    An Image object representing the generated image.
  """

  # Analyze the sentiment of the text.
  sentiment = TextBlob(text).sentiment.polarity

  # Choose an image based on the sentiment.
  if sentiment > 0:
    image_url = "https://example.com/positive.jpg"
  elif sentiment < 0:
    image_url = "https://example.com/negative.jpg"
  else:
    image_url = "https://example.com/neutral.jpg"

  # Download the image.
  response = requests.get(image_url)

  # Create an Image object from the downloaded image.
  image = Image.open(BytesIO(response.content))

  return image

# Get the user's text.
text = input("Enter some text: ")

# Create an image based on the sentiment of the text.
image = create_image_from_sentiment(text)

# Display the image.
image.show()


with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
            image.show()
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
            image.show()
        else:
            st.write( 'Es un sentimiento Neutral 😐')
            image.show()

