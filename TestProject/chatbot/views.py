import openai
from django.shortcuts import render
from django.http import JsonResponse

openai.api_key = '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'  # Replace with your OpenAI API key

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )

        reply = response.choices[0].text.strip()

        return JsonResponse({'message': reply})

    return render(request, 'chatbot/chat.html')
