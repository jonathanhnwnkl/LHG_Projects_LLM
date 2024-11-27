from langchain_ollama import OllamaLLM
import tkinter

model = OllamaLLM(model="llama3.2")

tkinter._test()

result = model.invoke(input="Hello, how are you?")
print(result)

template =  """ 

Categorise the project based on the following description and Project Name:



"""