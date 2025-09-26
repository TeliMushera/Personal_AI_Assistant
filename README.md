# 🧑‍💻 Personal AI Assistant  

A simple **AI-powered conversational assistant** built using the **FLAN-T5 model** from Hugging Face’s `transformers` library.  
It maintains a short chat history to provide context-aware responses and runs in the terminal as an interactive chatbot.  

---

## 🙌 Acknowledgements  

This project makes use of the following open-source resources:  

- [Hugging Face Transformers](https://huggingface.co/transformers/) – for providing the `pipeline` API and pretrained FLAN-T5 model.  
- [Google FLAN-T5](https://huggingface.co/google/flan-t5-large) – the model powering the assistant’s text generation.  
- [PyTorch](https://pytorch.org/) – backend framework for running deep learning models.  
- [Accelerate](https://huggingface.co/docs/accelerate) – for optimizing model performance.

---

## 📂 Code Overview  

The project code includes the following components:  

- **Imports & Model Initialization**  
  - Loads Hugging Face’s FLAN-T5 Large model using the `transformers` pipeline.  

- **Chat History Management**  
  - Stores conversation history in a list.  
  - Maintains the last 5 exchanges for context-aware replies.  

- **ask_ai() Function**  
  - Takes user input, updates history, generates a model response, and appends it back to history.  

- **Main Chat Loop**  
  - Runs an interactive loop in the terminal.  
  - Listens for user input, calls the assistant, and prints replies.  
  - Ends gracefully when the user types `exit`, `bye`, or `quit`.
