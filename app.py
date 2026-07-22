import streamlit as st, json
import google.generativeai as genai

st.set_page_config(page_title='Dormakaba AI Product Finder')
with open('products.json') as f:
    products=json.load(f)

st.title('🏨 Dormakaba AI Product Finder')
api_key=st.text_input('Gemini API Key',type='password')
industry=st.selectbox('Industry',['Hotel','Commercial','Education','Healthcare'])
requirements=st.text_area('Requirements','Mobile access, audit trail, contactless entry')

if st.button('Find Solutions'):
    catalog='\n'.join([f"{p['name']} - {p['description']}" for p in products])
    if api_key:
      genai.configure(api_key=api_key)
      model=genai.GenerativeModel('gemini-1.5-flash')
      prompt=f'''You are a Dormakaba solution advisor. Industry={industry}. Requirements={requirements}. Catalog:{catalog}. Recommend products, reasons, benefits, next steps.'''
      st.markdown(model.generate_content(prompt).text)
    else:
      st.warning('Enter Gemini API key')
