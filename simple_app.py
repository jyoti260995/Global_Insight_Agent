import streamlit as st
from agent import agent

st.set_page_config(
    page_title="Global Insight Agent",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Global Insight Agent")
st.write("Get current weather and latest news for any location.")

location = st.text_input("Enter location:", placeholder="Example: Delhi, Tokyo, London")

if st.button("Get Insights"):
    if not location.strip():
        st.warning("Please enter a location.")
    else:
        with st.spinner("Fetching weather and latest news..."):
            query = f"Give me current weather and latest news for {location}"

            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": query
                        }
                    ]
                }
            )

            final_answer = response["messages"][-1].content

            st.subheader(f"Insights for {location}")
            st.write(final_answer)