import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, warnings
import string
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report , confusion_matrix

clean_text = None
df = None
# to get rid of the stopwords
nltk.download('stopwords')
stopwords = set(stopwords.words('turkish'))

def read_data():
    # Load the dataset
    try:
        df = pd.read_csv("TurkishSMSCollection.csv", sep=';')
    except FileNotFoundError:
        warnings.warn("CSV file not found. Ensure 'TurkishSMSCollection.csv' is in the current directory.")
        return None

    # Drop unnecessary columns if they exist
    if "GroupText" in df.columns:
        df = df.drop(columns="GroupText", axis=1)

        return df

def about_data():
    df = read_data()

    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.any():
        warnings.warn(f"Missing values detected:\n{missing_values}")

    # Check for empty dataset
    if df.empty:
        warnings.warn("The dataset is empty. Please check the CSV file.")
        return None

    # Check distribution of labels
    label_counts = df["Group"].value_counts()
    if label_counts.empty:
        warnings.warn("No 'Group' labels found in the dataset.")
        return None
    elif len(label_counts) < 2:
        warnings.warn("The dataset might be imbalanced. Ensure at least SPAM and NORMAL categories exist.")

    # Save the data distribution plot
    save_dir = "notes"
    os.makedirs(save_dir, exist_ok=True)
    plot_path = os.path.join(save_dir, "sms_distribution.png")

    plt.figure(figsize=(8, 6))
    ax = sns.countplot(x="Group", data=df)
    plt.title("Distribution of SMS")
    plt.xlabel("Group (1: SPAM, 2: NORMAL)")
    plt.ylabel("Count")

    # Add exact values on top of the bars
    for bar in ax.patches:
        ax.annotate(f'{int(bar.get_height())}',
                    (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                    ha='center', va='bottom', fontsize=10)

    plt.savefig(plot_path, dpi=300, bbox_inches="tight")
    plt.close()  # Close the plot to avoid popping up

    print(f"Data distribution plot saved to: {plot_path}")

    return df

def clean_data():
    df = read_data()
    # Step2: clean text

    df["Message"] = df["Message"].str.lower()
    df["Message"] = df["Message"].str.translate(str.maketrans('', '', string.punctuation))
    df["Message"] = df["Message"].str.replace('\s+', ' ', regex=True)

    df["Message"] = df["Message"].apply(lambda x: ' '.join([
        word for word in x.split()
        if word not in stopwords
    ]))
    return df

def draw_wordcloud():
    # we can draw the word cloud, need to join messages to give as an input to wordcloud
    df = clean_data()
    cleaned_text = ' '.join(df["Message"])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)

    # Save the wordcloud
    save_dir = "notes"
    os.makedirs(save_dir, exist_ok=True)
    plot_path = os.path.join(save_dir, "wordcloud.png")

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Wordcloud", fontsize=16)

    plt.savefig(plot_path, dpi=300, bbox_inches="tight")
    plt.close()  # Close the plot to avoid popping up

    print(f"Wordcloud plot saved to: {plot_path}")

def create_model():
    # need to clean data first
    df = clean_data()
    global model, tfidf  # Declare global variables

    # split data
    X = df["Message"]
    y = df["Group"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # feature extraction
    tfidf = TfidfVectorizer(max_features=5000)
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)

    # MODEL1: logistic regression training
    model = LogisticRegression()
    model.fit(X_train_tfidf, y_train)

    # let's write the model evaluation into a file
    save_dir = "notes"
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, "model_evaluation.txt")

    y_pred = model.predict(X_test_tfidf)
    acc = accuracy_score(y_test, y_pred)

    conf_matrix = confusion_matrix(y_test, y_pred)

    class_report = classification_report(y_test, y_pred)

    # Write the results to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Accuracy:\n{acc}\n\n")
        file.write(f"Confusion Matrix:\n{conf_matrix}\n\n")
        file.write(f"Classification Report:\n{class_report}\n")

    print(f"Model evaluation results saved to: {file_path}")


def is_phishing_sms(sms_text):
    create_model()
    # Ensure sms_text is a list, even if a single string is provided
    if isinstance(sms_text, str):
        sms_text = [sms_text]  # Convert single string to a list

    texts_tfidf = tfidf.transform(sms_text)  # Using the global tfidf
    predictions = model.predict(texts_tfidf)  # Using the global model

    results = []
    for message, prediction in zip(sms_text, predictions):
        if prediction == 1:
            result = True
        else:
            result = False
    return result

# Step1: analyze the dataset
# Step2: clean text
# Step3: draw word cloud
# Step4: split data
# Step5: feature extraction, tf-idf
# Step6: model training and evaluation
# Step7: model evaluation




