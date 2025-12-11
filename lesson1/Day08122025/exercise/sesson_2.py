# Bài tập 1: Quản lý học viên & khóa học

students = [
    ("SV01", "Hoang Nam", 16),
    ("SV02", "Mi Chau", 18),
    ("SV03", "Trong Thuy", 19),
]

# a.

for student in students:
  id, name, age = student
  print(f"{id} - {name} ({age})")

# b.

scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

python_scores = [(id, name, scores[id]["python"]) for id, name, _ in students]
print('\n', python_scores)

#  c.

top_python_score = python_scores[0]
for score in python_scores:
  if score[2] > top_python_score[2]:
    top_python_score = score

print(f'\nTop Python: {top_python_score[1]} - {top_python_score[2]}')

# d.

courses = {"math", "python"}

courses.add("database")
print('\n', courses)

for id, _, _ in students:
  scores[id]["database"] = 0

print('\n', scores)

# Bài tập 2: Thống kê sản phẩm & hóa đơn

products = [
    (1, "Iphone 17 Pro Max 1T", 45_250_000),
    (2, "Iphone 16 Pro Max 1T", 30_150_000),
    (3, "Iphone 15 Pro Max 1T", 25_000_000),
    (4, "Iphone 11 Pro Max 1T", 10_500_000),
]

orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]

# a.

product_map = {product[0]: {"name": product[1], "price": product[2]} for product in products}
print('\n', product_map)

# b.

for order in orders:
  total = 0
  for id in order["items"]:
    total += product_map[id]["price"]
  order["total"] = total

print('\n', orders)

# c.
print('\n')
for order in orders:
  print(f'{order["order_id"]}: - {len(order["items"])} san pham, Tong tien = {order["total"]}')

# Bài tập 3: Hệ thống tag bài viết & người dùng

users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]

posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}

# a.

user_map = {user[0]: user[1] for user in users}
print('\n', user_map)

# b.

for post_id, post in posts.items():
  print(f'[{post_id}] {post["title"]} - {user_map[post["author_id"]]} - Tags: {", ".join(sorted(post["tags"]))}')

# c.
all_tags = set()

for post in posts.values():
  all_tags.update(post["tags"])

print('\n', all_tags)

# * d.

tag_counter = {tag: 0 for tag in all_tags}

for post in posts.values():
  for tag in post["tags"]:
    tag_counter[tag] += 1

print('\n', tag_counter)