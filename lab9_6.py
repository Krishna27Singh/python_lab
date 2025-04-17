def most_pages(data):
    max_pages = data[0]["pages"]
    for i in data:
        max_pages=max(max_pages,i["pages"])
    for i in data:
        if(i["pages"]==max_pages):
            answer = i["title"]
    return answer
     


data = [{"title":"book1", "author": "author1", "pages": 20},
        {"title":"book2", "author": "author2", "pages": 21},
        {"title":"book3", "author": "author3", "pages": 22},]

answer = most_pages(data)
print(answer)