import streamlit
import requests

api_key="xdSdXq9mY0hoDGDI2sJkOMEKDb52a5k2VRSfQCWx"
url="https://api.nasa.gov/planetary/apod?"\
    f"api_key={api_key}"
response1=requests.get(url)
data=response1.json()

title=data['title']
image_url=data['url']
explanation=data["explanation"]

image_filepath="img.png"
response2=requests.get(image_url)
with open(image_filepath,"wb") as file:
    file.write(response2.content)
streamlit.title(title)
streamlit.image(image_filepath)
streamlit.write(explanation)