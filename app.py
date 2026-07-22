
import streamlit as st
import json
import google.generativeai as genai

st.set_page_config(
    page_title="Dormakaba AI Product Finder",
    page_icon="🏨",
    layout="wide"
)

# Load Product Catalog
with open("products.json", "r") as f:
    products = json.load(f)

st.title("🏨 Dormakaba AI Product Finder")

api_key = st.text_input(
    "Gemini API Key",
    type="password"
)

industry = st.selectbox(
    "Industry",
    [
        "Hotel",
        "Commercial",
        "Education",
        "Healthcare"
    ]
)

requirements = st.text_area(
    "Requirements",
    placeholder="Example: Mobile access, contactless entry, audit trail"
)

if st.button("Find Solutions"):

    if not api_key:
        st.error("Please enter your Gemini API Key")
        st.stop()

    try:

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            "gemini-2.0-flash"
        )

        catalog = "\n".join(
            [
                f"""
Product: {p['name']}
Description: {p['description']}
Industry: {p['industry']}
"""
                for p in products
            ]
        )

        prompt = f"""
You are a Dormakaba Product Consultant.

Customer Industry:
{industry}

Requirements:
{requirements}

Available Products:
{catalog}

Provide:

1. Top Recommended Products
2. Why each product fits
3. Business Benefits
4. Suggested Next Steps

Use professional business language.
"""

        response = model.generate_content(prompt)

        st.subheader("Recommendations")

        st.markdown(response.text)

    except Exception as e:
        st.error(f"Error: {str(e)}")
