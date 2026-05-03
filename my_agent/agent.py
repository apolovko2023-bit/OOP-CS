from google.adk.agents import Agent
from tools import safe_divide, count_words


system_prompt = """
Ти навчальний Python-асистент.

Правила:
- Відповідай українською мовою
- Пояснюй просто і структуровано
- Якщо використовуєш інструменти — повертай короткий результат
- Завжди перевіряй коректність вводу
- Не вигадуй відповіді
"""


root_agent = Agent(
    name="my_agent",
    model="gemini-2.5-flash",
    instruction="Ти корисний навчальний асистент",
    tools=[]
)