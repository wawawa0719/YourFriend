from discord import welcome_screen
import google.generativeai as genai
import os
# API-KEYの設定

menSetText = "男前な男性"
womenSetText = "小学生"

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
gemini_pro = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def geminiCreateText(inputText):
  prompt = "以下に示す文章に、ルルーシュ・ランペルージのような口調で返信してください。「" + inputText + "」"
  response = gemini_pro.generate_content(prompt)
  print(response.text)
  return (response.text)
