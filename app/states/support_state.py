import reflex as rx
from typing import TypedDict


class FAQItem(TypedDict):
    question: str
    answer: str


class SupportState(rx.State):
    faq_items: list[FAQItem] = [
        {
            "question": "How do I reset my password?",
            "answer": "You can reset your password by going to the login page and clicking 'Forgot Password'. You will receive an email with instructions.",
        },
        {
            "question": "How do I update my billing information?",
            "answer": "You can update your billing information in the 'Billing' section of your account settings.",
        },
        {
            "question": "How can I track my order?",
            "answer": "Once your order has shipped, you will receive an email with a tracking number. You can use this number to track your order on the carrier's website.",
        },
        {
            "question": "What is your return policy?",
            "answer": "We offer a 30-day return policy for most items. Please visit our returns page for more details.",
        },
    ]