import streamlit as st
import hashlib

st.set_page_config(
    page_title="File Integrity Checker",
    page_icon="🔒",
    layout="centered"
)

st.title("🔒 File Integrity Checker")
st.write("Upload a file to generate and verify its SHA-256 hash.")

def calculate_hash(file):
    sha256 = hashlib.sha256()

    file.seek(0)
    while chunk := file.read(4096):
        sha256.update(chunk)

    file.seek(0)
    return sha256.hexdigest()

uploaded_file = st.file_uploader(
    "Choose a file",
    type=None
)

if uploaded_file is not None:

    current_hash = calculate_hash(uploaded_file)

    st.subheader("Generated SHA-256 Hash")
    st.code(current_hash)

    st.download_button(
        label="📥 Download Hash",
        data=current_hash,
        file_name="sha256_hash.txt",
        mime="text/plain"
    )

    st.subheader("Verify File Integrity")

    original_hash = st.text_input(
        "Paste Original SHA-256 Hash"
    )

    if st.button("Verify Integrity"):

        if original_hash.strip() == "":
            st.warning("Please enter an original hash.")

        elif original_hash.strip() == current_hash:
            st.success("✅ File Integrity Verified")
            st.balloons()

        else:
            st.error("❌ Warning! File Has Been Modified")
