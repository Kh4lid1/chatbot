import gradio as gr
import openai
openai.api_key = "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"

def generate_response(user_input):
    messages = [
        {"role": "system", "content": "Chat bot"},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response.choices[0].message.content
    return reply

def chatbot_interface(user_input):
    response = generate_response(user_input)
    return response


iface = gr.Interface(
    fn=chatbot_interface,
    inputs="text",
    outputs="text",
    title="SNS Chat-Bot",
    description="Ask me anything!",
    theme=gr.themes.Soft(),
    layout="vertical",
    examples=[

        ["Who is the current King of the Kingdom of Saudi Arabia?"],
        ["What is SAP?"],
        ["Tell me a joke."]
    ],
    css="""
    #warning {background-color: #FFCCCB} 
    .feedback textarea {font-size: 24px !important}
    """
)

iface.launch()