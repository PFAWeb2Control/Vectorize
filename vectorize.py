import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

def usage():
    print("Usage:")
    print("python %s <data_dir>" % sys.argv[0])

if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    data_dir = sys.argv[1]
    classes = ['event', 'not']

    # Read the data
    train_data = []
    train_labels = []
  
    for curr_class in classes:
        dirname = os.path.join(data_dir, curr_class)
        for fname in os.listdir(dirname):
            with open(os.path.join(dirname, fname), 'r') as f:
                content = f.read()
                
                train_data.append(content)
                train_labels.append(curr_class)

    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=3,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True,decode_error='ignore')
    train_vectors = vectorizer.fit_transform(train_data)
    

  
