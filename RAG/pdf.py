from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document loaders\\notes.pdf")

print(data.load()[0].page_content)