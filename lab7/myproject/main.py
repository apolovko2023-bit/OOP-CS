import requests

def get_random_fact():
    # Надійне API з фактами про тварин
    url = "https://catfact.ninja/fact"
    
    print("🚀 Отримуємо цікавий факт через Poetry та Requests...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print("\n✅ Успішно! Ось ваш факт:")
        print(f"💡 {data['fact']}")
        
    except Exception as e:
        print(f"❌ Навіть це API дало збій: {e}")

if __name__ == "__main__":
    get_random_fact()