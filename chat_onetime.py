import requests

with open('D:/Researching/ChatGPT_API_Project/Script_and_data/excel_data/resume_test.txt', 'r', encoding='utf-8') as file:
    data1 = file.read()
resume_data = str(data1)

with open('D:/Researching/ChatGPT_API_Project/Script_and_data/excel_data/requirement.txt', 'r', encoding='utf-8') as file:
    data2 = file.read()
requirement_data = str(data2)



api_endpoint = 'https://api.openai.com/v1/chat/completions'
api_key = 'Your ChatGPT API key'

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
  "model": "gpt-3.5-turbo-0301",
  "messages": [{"role": "system","content": "คุณเป็นคนที่จะประเมินคะแนนสำหรับ Resume ว่า Resume นี้มีความเกี่ยวข้องกับรายละเอียดของงานหรือไม่ ถ้า skill ใน resume มีความเกี่ยวข้องน้อย คุณจะต้องให้คะแนนที่น้อย ส่วนถ้าคนที่มี skill ใน resume เยอะ คุณจะให้คะแนนเยอะ และช่วยบอกด้วยว่าแต่ละคะแนนที่คุณให้ คุณให้เพราะอะไร"},
               {"role":"user","content":"ฉันกำลังหาคนที่สามารถทำงานนี้ได้ ซึ่งรายละเอียดของ skill ที่ต้องการมีดังนี้ "+ requirement_data + "คุณช่วยดู Resume นี้ให้หน่อย ถ้าเค้ามี skill ตามที่ได้บอกไป ให้ คะแนน คือ 1 แต่ถ้าไม่มี ก็ให้ 0.\n\n"+resume_data + "\n\n Please provide format of answer like this (Python : 1 \n\n English : 0 \n\nWork Experience 2 years : 0\n\n Power automate : 1)"}
               ]
}
response = requests.post(api_endpoint, headers=request_headers ,json=request_data)
# print(response.content)
output = response.json()['choices'][0]['message']['content']
print(f"ChatGPT : {output}")