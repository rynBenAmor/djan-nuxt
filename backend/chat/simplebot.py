# ! unused but has potential
import re

class SimpleQABot:
    def __init__(self):
        self.response = ""
        # Expanded questions and answers with variations
        self.common_questions = {
            r'hello|hi|hey': 'Hi, how may I help you today?',
            r'car payment|pay.*car|car bill': 'Sure, I will provide you with our customer support number right away.',
            r'customer support|help|assist': 'You can reach our customer support at 1-800-123-4567.',
            r'thank(s| you)?': 'You\'re welcome! Anything else I can help with?',
            r'bye|goodbye|see you': 'Goodbye! Have a great day!',
            r'what.*your name': 'I am SimpleQABot, your assistant.',
            r'how are you': 'I am just code, but I am here to help you!',
        }

    def responder(self, user_input):
        for pattern, answer in self.common_questions.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return answer
        return "Sorry, I didn't understand that. Can you rephrase?"

    def add_qa(self, pattern, answer):
        """Add a new question/answer pattern."""
        self.common_questions[pattern] = answer

# Usage: Loop for multiple questions
if __name__ == "__main__":
    bot = SimpleQABot()
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = bot.responder(user_input)
        print("Bot:", response)
        if re.search(r'bye|goodbye', user_input, re.IGNORECASE):
            break



"""

fetch('/chatbot/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]')  // CSRF protection
    },
    body: JSON.stringify({ text: userInput })  // send user message
})
.then(res => res.json())
.then(data => {
    console.log('Bot says:', data.response);
});


def chatbot_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            bot = SimpleQABot()
            response = bot.responder(user_input=text)
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)
"""