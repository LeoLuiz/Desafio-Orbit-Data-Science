import requests
import csv

url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)

# Verifica se a requisição foi atendida
if response.status_code == 200:
    comments = response.json()
    csv_filename = "comments.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['postId', 'id', 'name', 'email', 'body'])
        for comment in comments:
            csv_writer.writerow([comment['postId'], comment['id'], comment['name'], comment['email'], comment['body']])

    print("Os comentários foram exportados para {csv_filename}")
else:
    print("A requisição falhou!")
