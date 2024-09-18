import streamlit as st
from scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content

from parse import parse_with_ollama

st.title("AI web scraper")
url=st.text_input("Enter a website URL:")

if st.button("Scrape site"):
  st.write("Scraping the website")
  result=scrape_website(url)
  body_content=extract_body_content(result)
  clean_content=clean_body_content(body_content)
  st.session_state.dom_content=clean_content
  
  with st.expander("View DOM content"):
    st.text_area("DOM content",clean_content,height=300)

if "dom_content" in st.session_state:
  parse_description=st.text_area("Describe what you want to parser")
  if st.button(" parse content"):
    if parse_description:
      st.write("parseing the content")
      dom_chunks=split_dom_content(st.session_state.dom_content)
      result=parse_with_ollama(dom_chunks,parse_description)
      st.write(result)