import gradio as gr

def say_ah():
    return "��."

demo = gr.Interface(
    fn=say_ah,
    inputs=None,
    outputs=gr.Textbox(label="���")
)

demo.launch()