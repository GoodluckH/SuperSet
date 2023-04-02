from io import BytesIO

import fitz
import markdown2
import streamlit as st
from xhtml2pdf import pisa

from engine import generate_problem_set
from prompt import generate_textbook_prompt_template

st.write("# SuperSet")

st.markdown("------")


uploaded_file = st.file_uploader("Upload your textbook", type="pdf")
excerpt = ""
if uploaded_file is not None:
    # parse the pdf
    ibuffer = BytesIO(uploaded_file.getvalue())
    pdf = fitz.open("pdf", ibuffer)

    user_selected_range = [0, 0]

    col1, col2 = st.columns(2)

    with col1:
        user_selected_range[0] = st.number_input(
            "Start Page", min_value=1, max_value=pdf.page_count, value=1)
    with col2:
        user_selected_range[1] = st.number_input(
            "End Page", min_value=user_selected_range[0], max_value=pdf.page_count, value=user_selected_range[0])

    excerpt = ""
    for i in range(user_selected_range[0], user_selected_range[1]):
        excerpt += pdf[i].get_text()

num_questions = st.slider("Number of questions",
                          min_value=1,
                          max_value=50,
                          value=20)

if st.button("Generate"):
    problem_set = None
    with st.spinner("Generating problem set..."):
        problem_set = generate_problem_set(
            generate_textbook_prompt_template(),
            num_questions=num_questions,
            excerpt=excerpt,
        )
    with st.expander(label="**Show problem set**"):
        st.write(problem_set)

    html = markdown2.markdown(problem_set)
    output = BytesIO()
    pisa_status = pisa.CreatePDF(bytes(str(html), "utf-8"),
                                 dest=output,
                                 encoding="utf-8")
    st.download_button(
        "Download as PDF",
        data=output.getvalue(),
        file_name="output.pdf",
        mime='application/pdf',
    )
