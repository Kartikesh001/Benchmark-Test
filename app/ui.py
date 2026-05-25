import uuid
import gradio as gr

from app.memory import save_message, get_history
from app.oss_assistant import generate_response as oss_response
from app.frontier_assistant import generate_response as frontier_response
from app.safety import is_safe, refusal_message

SESSION_ID = str(uuid.uuid4())


def respond(message, history, model_choice):

    if not is_safe(message):
        return refusal_message()

    conversation = get_history(SESSION_ID)

    if model_choice == "Open Source (Qwen)":
        response = oss_response(message, conversation)
    else:
        response = frontier_response(message, conversation)

    save_message(SESSION_ID, "user", message)
    save_message(SESSION_ID, "assistant", response)

    return response


with gr.Blocks() as demo:

    gr.Markdown("# AI Assistant Comparison")

    model_choice = gr.Dropdown(
        choices=[
            "Open Source (Qwen)",
            "Frontier (Gemini)"
        ],
        value="Open Source (Qwen)",
        label="Assistant"
    )

    chatbot = gr.Chatbot(height=500)

    msg = gr.Textbox(
        placeholder="Type your message..."
    )

    clear = gr.Button("Clear Chat")

    def user_chat(message, history, model_name):
        response = respond(
            message,
            history,
            model_name
        )

        history.append(
            (message, response)
        )

        return "", history

    msg.submit(
        user_chat,
        inputs=[
            msg,
            chatbot,
            model_choice
        ],
        outputs=[
            msg,
            chatbot
        ]
    )

    clear.click(
        lambda: [],
        None,
        chatbot
    )

demo.launch()