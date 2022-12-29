from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.8vasl6v.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# (1) 영화제목 '가버나움'의 평점을 가져오기
movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])

# (2) '가버나움'의 평점과 같은 평점의 영화 제목들을 가져오기
star = movie['star']
all_movies = list(db.movies.find({'star':star},{'_id':False}))
for movie2 in all_movies:
    print(movie2['title'])

# (3) '가버나움' 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})  # star가 문자열로 저장되어 있어서, 양식에 맞추기 위해 '0'

