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


def about_data():
    # Load the dataset
    try:
        df = pd.read_csv("TurkishSMSCollection.csv", sep=';')
    except FileNotFoundError:
        warnings.warn("CSV file not found. Ensure 'TurkishSMSCollection.csv' is in the current directory.")
        return None

    # Drop unnecessary columns if they exist
    if "GroupText" in df.columns:
        df = df.drop(columns="GroupText", axis=1)

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

def clean_data(df, stopwords):
    df["Message"] = df["Message"].str.lower()
    df["Message"] = df["Message"].str.translate(str.maketrans('', '', string.punctuation))
    df["Message"] = df["Message"].str.replace('\s+', ' ', regex=True)



    df["Message"] = df["Message"].apply(lambda x: ' '.join([
        word for word in x.split()
        if word not in stopwords
    ]))
    return df

def draw_wordcloud(df):
    # we can draw the word cloud, need to join messages to give as an input to wordcloud
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

def model_evaluation(X_test_tfidf, y_test):
    y_pred = model.predict(X_test_tfidf)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc}")

    conf_matrix = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(conf_matrix)

    class_report = classification_report(y_test, y_pred)
    print("Classification Report:")
    print(class_report)

def is_phishing_sms(sms_text):
    # Ensure sms_text is a list, even if a single string is provided
    if isinstance(sms_text, str):
        sms_text = [sms_text]  # Convert single string to a list

    texts_tfidf = tfidf.transform(sms_text)
    predictions = model.predict(texts_tfidf)

    for message, prediction in zip(sms_text, predictions):
        if prediction == 1:
            result = print(f"'{message}' : Spam")
        else:
            result= print(f"'{message}' : Normal")
    return result

if __name__ == '__main__':
    # Step1: analyze the dataset
    df = about_data()

    # Step2: clean text
    # to get rid of the stopwords
    nltk.download('stopwords')
    stopwords = set(stopwords.words('turkish'))

    df = clean_data(df, stopwords)

    # Step3: draw word cloud
    draw_wordcloud(df)

    # Step4: split data
    X = df["Message"]
    y = df["Group"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step5: feature extraction, tf-idf
    tfidf = TfidfVectorizer(max_features=5000)
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)

    # Step6: model training and evaluation
    # MODEL1: logistic regression training
    model = LogisticRegression()
    model.fit(X_train_tfidf, y_train)
    # model evaluation
    model_evaluation(X_test_tfidf, y_test)

    # take sms input and classify it as spam or not using the model
    # MODEL2:




