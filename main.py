import math
import os.path
import re

base_dir = os.path.join(os.getcwd(),'search_engine_dataset')

def load_files():
    """loads the files from base directory and saves them into a dictionary
    whose keys are file name and values are file's content"""
    files = {}
    for filename in os.listdir(base_dir):
        file_path = os.path.join(base_dir,filename)
        file = filename.split('.')[0]
        if os.path.isfile(file_path):
            with open(file_path,'r',encoding='utf8') as f:
                files[file] = f.read()
    return files

def preprocess(files: dict):
    """breaks content of each file into lower case words and removes
     stopwords and punctuation"""
    files_processed = {}
    stopword = {"is", "the", "and", "of", "to", "in", "a"}

    for filename, text in files.items():
        text_lower = text.lower()
        text_processed = re.sub(r'[^a-zA-Z0-9\s]',"",text_lower)

        text_split = text_processed.split()
        words = [text for text in text_split if text not in stopword]
        files_processed[filename] = words
    # print(files_processed)
    return files_processed

def inverted_index(files: dict):
    inverted_dict = {}
    for key, values in files.items():
        for val in values:
            if val not in inverted_dict:
                inverted_dict[val] = set()
            inverted_dict[val].add(key)

    return inverted_dict

def user_query(query):

    stopword = {"is", "the", "and", "of", "to", "in", "a", "are", "was",
                "were", "had", "have", "am"}

    query_lower = query.lower()
    query_processed = re.sub(r'[^a-zA-Z0-9\s]',"",query_lower)
    query_split = query_processed.split()
    final_query = [word for word in query_split if word not in stopword]

    return final_query

def lookup(query: list, inverted_dict: dict):
    result = {}
    for token in query:
        if token in inverted_dict:
            result[token] = inverted_dict[token]

    return result

def calculate_tfidf(query: list, matched_docs: dict, docs: dict):
    score = {}
    total_docs = len(docs)

    for token in query:
        if token not in matched_docs:
            continue

        docs_with_token = matched_docs[token]

        idf = math.log(total_docs/len(docs_with_token))

        for filename in docs_with_token:
            words = docs[filename]
            # print(type(words))
            total_words = len(words)

            word_count = words.count(token)
            tf = word_count/total_words

            tfidf = tf * idf

            if filename not in score:
                score[filename] = 0
            score[filename] += tfidf


    ranked = sorted(score.items(),key= lambda x:x[1] ,reverse=True)
    return ranked

def get_result(rankings,data):
    outputs = []
    for i,(filename, score) in enumerate(rankings[:5]):
        snippet = "".join(data[filename][:35])
        output = f"{i+1}. {filename}: (score: {round(score, 4)})\n"
        output += f"\t{snippet}...\n"
        outputs.append(output)

    return "\n".join(outputs)


if __name__ == "__main__":
    data = load_files()
    processed_data = preprocess(data)
    inverted_dict = inverted_index(processed_data)

    query = input("What is your query: ")
    query_processed = user_query(query)
    result = lookup(query_processed, inverted_dict)
    rankings = calculate_tfidf(query_processed,result, processed_data)
    output = get_result(rankings,data)

    print(output)

