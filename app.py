
import validators
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import (
    YoutubeLoader,
    UnstructuredURLLoader
)


## Streamlit APP
st.set_page_config(
    page_title="LangChain: Summarize Text From YT or Website",
    page_icon="🦜"
)

st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")


## Get the Groq API Key
with st.sidebar:
    groq_api_key = st.text_input(
        "Groq API Key",
        value="",
        type="password"
    )

generic_url = st.text_input(
    "URL",
    label_visibility="collapsed"
)


## Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=groq_api_key,
    temperature=0
)


## Prompt
prompt_template = """
Provide a summary of the following content in 300 words.

Content:
{text}
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["text"]
)


if st.button("Summarize the Content from YT or Website"):

    ## Validate inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")

    elif not validators.url(generic_url):
        st.error(
            "Please enter a valid URL. "
            "It can be a YouTube video URL or website URL."
        )

    else:

        try:

            with st.spinner("Waiting..."):

                ## Load YouTube or Website data

                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                    generic_url,
                    add_video_info=False,
                    language=["en-IN", "en", "hi"]
                    )
                else:

                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={
                            "User-Agent": (
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 "
                                "(KHTML, like Gecko) "
                                "Chrome/116.0.0.0 Safari/537.36"
                            )
                        }
                    )

                docs = loader.load()

                ## Combine document content
                text = "\n\n".join(
                    doc.page_content for doc in docs
                )

                ## Create the prompt
                formatted_prompt = prompt.format(
                    text=text
                )

                ## Send prompt to Groq
                response = llm.invoke(
                    formatted_prompt
                )

                ## Get the generated summary
                output_summary = response.content

                ## Display result
                st.success(output_summary)

        except Exception as e:

            st.exception(e)

