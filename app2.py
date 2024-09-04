import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import os

## Function to get response from LLama model
def get_social_media_caption(topic, platform, tone, max_length):
    # Specify the path to your local model file
    model_path = 'D:\model\model\llama-2-7b-chat.ggmlv3.q8_0.bin'

    # Check if the model file exists
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}. Please check the file path.")
        return None

    ### LLama2 model
    llm = CTransformers(model=model_path,
                        model_type='llama',
                        config={'max_new_tokens': 64,
                                'temperature': 0.7})  # Increased temperature for more creative outputs
    
    ## Prompt Template
    template = """
    Create an engaging social media caption for {platform} about {topic}.
    The tone should be {tone}.
    Include relevant emojis throughout the caption.
    The caption should be no longer than {max_length} characters.
    Make sure the emojis are appropriate for the content and enhance the message.
    """
    
    prompt = PromptTemplate(input_variables=["platform", "topic", "tone", "max_length"],
                            template=template)
    
    ## Generate the response from the LLama 2 model
    response = llm.invoke(prompt.format(platform=platform, topic=topic, tone=tone, max_length=max_length))
    print(response)
    return response

st.set_page_config(page_title="Generate Social Media Captions",
                    page_icon='📱',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Social Media Captions 📱✨")

topic = st.text_input("Enter the Topic for your post")

## Creating two more columns for additional fields

col1, col2 = st.columns([5,5])

with col1:
    platform = st.selectbox('Choose the social media platform',
                            ('Instagram', 'Twitter', 'LinkedIn', 'TikTok'),
                            index=0)
with col2:
    tone = st.selectbox('Select the tone of the caption',
                        ('Friendly', 'Professional', 'Humorous', 'Inspirational'),
                        index=0)

max_length = st.slider('Maximum caption length', 50, 280, 150)

submit = st.button("Generate Caption")

## Final response
if submit:
    with st.spinner("Generating your caption..."):
        caption = get_social_media_caption(topic, platform, tone, max_length)
        if caption:
            st.text_area("Generated Caption", caption, height=150)
            st.info(f"Character count: {len(caption)}")