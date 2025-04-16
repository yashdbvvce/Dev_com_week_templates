from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch
from langchain_google_genai import ChatGoogleGenerativeAI
import lorem

# Load environment variables from .env
load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')


#============================================================================================================
# Define prompt templates for different feedback types - Modify the prompts for more finetuning
positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a feedback response generator. Reply only with the message. No bullet points, notes, or explanations."),
        ("human", "Write a thank-you note for this positive feedback: {feedback}. Only return the message, nothing else."),
    ]
)


negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a feedback response generator. Reply only with the message. No explanations or extra information."),
        ("human", "Write a professional apology or resolution for this negative feedback: {feedback}. Only return the response message."),
    ]
)


neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a feedback response generator. Reply only with the message. Do not add bullet points or notes."),
        ("human", "Write a message asking for more details about this neutral feedback: {feedback}. Only return the message."),
    ]
)


escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a feedback responder. Return only a short message for escalation."),
        ("human", "Generate a message to escalate this feedback to a human agent: {feedback}. Only return the message."),
    ]
)


#============================================================================================================

# Define the feedback classification template
classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a sentiment classifier."),
        ("human",
         "Classify the sentiment of this customer feedback strictly as one word only from the list [positive, negative, neutral, escalate]: {feedback}. Do not provide any explanation or extra text."),
    ]
)



# Define the runnable branches for handling feedback
branches = RunnableBranch(
    (
        lambda x: "positive" in x,
        positive_feedback_template | model | StrOutputParser()  # Positive feedback chain
    ),
    (
        lambda x: "negative" in x,
        negative_feedback_template | model | StrOutputParser()  # Negative feedback chain
    ),
    (
        lambda x: "neutral" in x,
        neutral_feedback_template | model | StrOutputParser()  # Neutral feedback chain
    ),
    escalate_feedback_template | model | StrOutputParser()
)



def generate_response(feedback):
    # Construct the chain

    # Get the result from the chain

    # return a valid result
    return lorem.paragraph()
