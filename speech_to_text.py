import speech_recognition as sr
import nltk
from transformers import pipeline
import pyttsx3

def main():
    nltk.download('punkt')  # Download NLTK data

    r = sr.Recognizer()
    engine = pyttsx3.init()  # Initialize text-to-speech engine

    while True:
        with sr.Microphone() as source:
            print("Listening for wake word")
            engine.say("Listening for wake word")
            engine.runAndWait()

            r.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise

            try:
                audio = r.listen(source, timeout=5)  # Listen with a timeout

                # Trigger word detection
                trigger_text = r.recognize_google(audio)
                if "barbie" in trigger_text.lower():
                    print("Murali")
                    engine.say("Hey Murali, how can I help you?")
                    engine.runAndWait()

                    # Ask for user's query
                    print("Listening for your query...")
                    engine.say("Listening for your query...")
                    engine.runAndWait()

                    audio = r.listen(source, timeout=10)  # Listen for query with a longer timeout
                    query = r.recognize_google(audio)

                    print("User's Query:", query)

                    # Apply NLP processing
                    processed_text = nlp_process(query)

                    # Write processed text to a file
                    with open("processed_query.txt", "w") as file:
                        file.write(processed_text)

                    print("Processed text saved to 'processed_query.txt'.")

                    break  # Exit the loop after successful query processing

                else:
                    print("Trigger not detected. Please try again.")

            except sr.WaitTimeoutError:
                print("No audio detected. Please try again.")

            except sr.UnknownValueError:
                print("Could not understand audio. Please try again.")

    engine.stop()  # Stop the text-to-speech engine

def nlp_process(text):
    # Tokenization, removing stopwords, and stemming using NLTK
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer

    # Tokenization
    tokens = word_tokenize(text)

    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    processed_text = f"NLP processing result for: {text}\nTokens: {stemmed_tokens}"
    return processed_text

if _name_ == "_main_":
    main()