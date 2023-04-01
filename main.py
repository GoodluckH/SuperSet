from io import BytesIO

import fitz
import markdown2
import streamlit as st
from xhtml2pdf import pisa

from engine import generate_problem_set
from prompt import generate_simple_prompt_template

st.write("# fkexams")

st.markdown("------")

# # upload file
# uploaded_file = st.file_uploader("Upload your textbook", type="pdf")

# if uploaded_file is not None:
#     # parse the pdf
#     ibuffer = BytesIO(uploaded_file.getvalue())
#     pdf = fitz.open("pdf", ibuffer)
#     toc = pdf.get_toc(simple=False)

#     # display the table of contents with hierarchy, for each toc item,
#     # make a checkbox
#     user_selected_pages = []
#     for i, entry in enumerate(toc):
#         level = entry[0]
#         title = entry[1]
#         page = entry[2]
#         st.markdown(f"{'##' * level} {title}")

#         # checkbox
#         if st.checkbox("", key=i):
#             # compute the page range from selected toc item to the next
#             # toc item
#             if i == len(toc) - 1:
#                 page_range = [page, pdf.page_count]
#             else:
#                 page_range = [page, toc[i + 1][2]]

#             if (page_range[0] <= page_range[1]):
#                 user_selected_pages.append(page_range)

#     # display the selected pages
#     st.write("## Selected pages")
#     st.write(user_selected_pages)

# dropdown to choose textbook
textbook = st.selectbox("Choose your textbook", [
    "Computer Networks (5th Edition) by Andrew S. Tanenbaum and David Wetherall"
])

chapters = st.text_input(
    "Enter the chapters you want to generate questions for (separated by commas)",
    value="5.5, 5.6.0-5.6.4")

num_questions = st.slider("Number of questions",
                          min_value=1,
                          max_value=20,
                          value=5)

if st.button("Generate", disabled=textbook is None or chapters is None):
    problem_set = None
    with st.spinner("Generating problem set..."):
        problem_set = generate_problem_set(
            generate_simple_prompt_template(),
            textbook=textbook,
            chapters=chapters,
            num_questions=num_questions,
        )
    with st.expander(label="**Show problem set**"):
        st.write(problem_set)

    print(problem_set)
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

# problem_set = """
# #### 5.5

# 1. Describe the differences between the connectionless and connection-oriented services in the Internet protocol suite.
# 2. Explain how the reliability of connection-oriented services is achieved through the use of acknowledgments.
# 3. Explain why the connection-oriented services require that the network topology be known in advance.
# 4. Describe the differences between the sliding window and the stop-and-wait protocols.
# 5. Describe the three-way handshake used to establish a connection in the TCP protocol.

# #### 5.6.0

# 1. What is the purpose of the Internet Control Message Protocol (ICMP)?
# 2. Explain how ICMP can be used to debug a network.
# 3. Describe how ICMP can be used to detect network congestion.
# 4. What is the purpose of the traceroute program?
# 5. Explain how the traceroute program uses ICMP to detect the route of a packet.

# #### 5.6.1

# 1. What is the purpose of the Domain Name System (DNS)?
# 2. Explain how DNS can be used to map a domain name to an IP address.
# 3. Describe the structure of a DNS query and how it is used to look up a domain name.
# 4. Explain the differences between authoritative and recursive DNS queries.
# 5. Describe how DNS can be used to provide load balancing for a server.

# #### 5.6.2

# 1. What is the purpose of the Address Resolution Protocol (ARP)?
# 2. Explain how ARP is used to map an IP address to a MAC address.
# 3. Describe the structure of an ARP request and how it is used to look up a MAC address.
# 4. Explain the differences between static and dynamic ARP.
# 5. Describe how ARP can be used to detect a malicious node on the network.

# #### 5.6.3

# 1. What is the purpose of the Reverse Address Resolution Protocol (RARP)?
# 2. Explain how RARP is used to map a MAC address to an IP address.
# 3. Describe the structure of a RARP request and how it is used to look up an IP address.
# 4. Explain the differences between static and dynamic RARP.
# 5. Describe how RARP can be used to detect a malicious node on the network.

# #### 5.6.4

# 1. What is the purpose of the Internet Group Management Protocol (IGMP)?
# 2. Explain how IGMP is used to detect changes in the membership of a multicast group.
# 3. Describe the structure of an IGMP message and how it is used to join or leave a multicast group.
# 4. Explain the differences between IGMPv1, IGMPv2, and IGMPv3.
# 5. Describe how IGMP can be used to detect a malicious node on the network.
# """

# with st.expander(label="**Show problem set**"):
#     st.write(problem_set)

# print(problem_set)
# html = markdown2.markdown(problem_set)
# output = BytesIO()
# pisa_status = pisa.CreatePDF(bytes(str(html), "utf-8"),
#                                 dest=output,
#                                 encoding="utf-8")
# st.download_button(
#     "Download as PDF",
#     data=output.getvalue(),
#     file_name="output.pdf",
#     mime='application/pdf',
# )
