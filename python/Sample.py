from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 인스턴스 생성
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# 인덱스 생성
index_name = 'sample_index'
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# 예제 데이터 생성
sample_data = [
    {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    },
    {
        'name': 'Jane Smith',
        'age': 25,
        'city': 'Los Angeles'
    },
    {
        'name': 'Bob Johnson',
        'age': 35,
        'city': 'Chicago'
    }
]

# 데이터 색인화
for i, data in enumerate(sample_data):
    es.index(index=index_name, doc_type='_doc', id=i+1, body=data)

# 데이터 확인
res = es.search(index=index_name, body={'query': {'match_all': {}}})
print(res)
