import json
import redis

def print_redis_data():
    # Подключаемся к Redis
    redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    # Получаем все ключи
    keys = redis_client.keys('*')
    
    print("=== Данные в Redis ===")
    for key in keys:
        print(f"\nКлюч: {key}")
        value = redis_client.get(key)
        try:
            # Пробуем распарсить JSON
            parsed_value = json.loads(value)
            print("Значение (JSON):")
            print(json.dumps(parsed_value, indent=2, ensure_ascii=False))
        except:
            # Если не JSON, выводим как есть
            print(f"Значение: {value}")
        
        # Показываем TTL
        ttl = redis_client.ttl(key)
        print(f"TTL: {ttl} секунд")

if __name__ == "__main__":
    print_redis_data() 