import streamlit as st

st.set_page_config(
    page_title="Document Search Engine",
    page_icon="📄"
)

st.title("📄 Document Search Engine")

uploaded_file = st.file_uploader(
    "Upload a Text File",
    type=["txt"]
)

if uploaded_file is not None:
    try:
        document = uploaded_file.read().decode("utf-8")

        st.subheader("Document Preview")
        st.text_area(
            "Content",
            document[:1000],
            height=200
        )

        query = st.text_input("Search Keyword")

        if query:
            lines = document.split("\n")

            results = [
                line for line in lines
                if query.lower() in line.lower()
            ]

            st.subheader(f"Search Results ({len(results)})")

            if results:
                for result in results:
                    st.write("✅", result)
            else:
                st.warning("No matching text found.")

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload a .txt file to begin.")
