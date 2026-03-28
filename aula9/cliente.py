import requests

# GET
res = requests.get("http://localhost:5000/produtos")
print("Lista de produtos:", res.json())

# POST
novo = {
    "id": 2,
    "nome": "Mouse",
    "preco": 100
}

res_post = requests.post("http://localhost:5000/produtos", json=novo)
print("Resposta POST:", res_post.json())
