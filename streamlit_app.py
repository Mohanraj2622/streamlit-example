import pandas as pd
import streamlit as st

# Load the CSV dataset
@st.cache
def load_data():
    return pd.read_csv('amazon_categories.csv')

data = load_data()

# Create a Streamlit app
st.title('Product Recommendation System')

# User input for search query
search_query = st.text_input('Search for a product:')

# Filter the dataset based on the search query
filtered_data = data[data['Product_Name'].str.contains(search_query, case=False)]

# Display recommendations
if not filtered_data.empty:
    st.subheader('Recommended Products:')
    st.dataframe(filtered_data)
else:
    st.write('No products found matching your search query.')


