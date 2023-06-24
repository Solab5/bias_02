import streamlit as st # web app
import spacy # named entity recognition

st.title("News Bias Words Recognizer")

# wait until the modl loads with a simple spinner - progress bar
with st.spinner("Please wait while the model is eing loaded...."):
    nlp = spacy.load("en_pipeline")

## text box to get user input

input = st.text_area(label = "Enter your text to get biased words recognized .......")

# create a doc object
doc = nlp(input)

# visualize the output

output_html = spacy.displacy.render(doc, style="ent", jupyter=False, options={"colors":{'bias':"#ff5136"}})

st.markdown(output_html, unsafe_allow_html=True)