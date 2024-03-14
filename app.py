from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title('Análisis de Sentimiento')
image = Image.open('emoticones.jpg')
st.image(image)
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

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
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

sentiment = blob.sentiment.polarity
recommendations = []
  if sentiment > 0:
    recommendations.append("It seems like you're feeling positive. Keep up the good work!")
    recommendations.append("Try to focus on the things that make you happy.")
  elif sentiment < 0:
    recommendations.append("It sounds like you're feeling down. That's okay. Everyone feels down sometimes.")
    recommendations.append("Try to talk to someone you trust about how you're feeling.")
    recommendations.append("There are also many resources available to help you cope with difficult emotions.")
  else:
    recommendations.append("It seems like you're feeling neutral. That's okay too.")
    recommendations.append("Try to find something to do that you enjoy.")

  # Return the results.
  return {
    "sentiment": sentiment,
    "recommendations": recommendations
  }

# Example usage:
text = "I'm feeling really down today."
results = analyze_text(text)

print(f"Sentiment: {results['sentiment']}")
print("Recommendations:")
for recommendation in results["recommendations"]:
  print(f"- {recommendation}")
