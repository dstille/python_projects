import sys, re

def readfile(fname):
    with open(fname, mode="r") as file:
        contents = file.read()
    return contents

def create_doc_dict(contents):
    doc_dict = {}
    raw_docs =re.split(r'<DOC>', contents.strip())
    for raw_doc in [rd for rd in raw_docs if rd != '']:
        doc_id = re.search(r'<DOCNO>(.+)</DOCNO>', raw_doc).group(1)
        doc = clean_doc(raw_doc)
        doc_dict[doc_id] = doc
    return doc_dict

def clean_doc(raw_doc):
    processed_doc = re.sub(r'<DOCNO>.+</DOCNO>', '', raw_doc)
    processed_doc = re.sub(r'<(/)?DOC>', '', processed_doc) 
    processed_doc = re.sub(r'<(/)?TEXT>', '', processed_doc)  
    return processed_doc.strip()     


def main():
    contents = readfile('all-senate-speeches.txt')
    doc_dict = create_doc_dict(contents)
    for doc_id in list(doc_dict.keys())[:10]:
        print(doc_id)
        print(doc_dict[doc_id])


if __name__ == '__main__':
    main()