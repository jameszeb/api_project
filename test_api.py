from api_project import *



def test_create_post_returns_post_data():
    status_code, post = create_post('test title','test body')
    assert status_code == 201
    assert post['title'] == 'test title'
    assert post['body'] == 'test body'

def test_get_title_body_id_returns_json_title():
    url = "https://jsonplaceholder.typicode.com"
    body = 'ullam et saepe reiciendis voluptatem adipisci sit amet autem assumenda provident rerum culpa quis hic commodi nesciunt rem tenetur doloremque ipsam iure quis sunt voluptatem rerum illo velit'
    choice = 4
    post = requests.get(f'{url}/posts/{choice}')
    assert post.json()['title'] == 'eum et est occaecati'
    assert post.json()['id'] == choice
    assert 'ullam et saepe reiciendis voluptatem' in body

def test_get_show_posts():
    limit = 15
    id = 15
    request = requests.get(f'{url}/posts?limit={limit}', params={'_limit': limit})
    request.raise_for_status()
    post = request.json()
    assert post[id-1]['id'] == 15



