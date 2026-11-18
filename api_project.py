import requests

url = "https://jsonplaceholder.typicode.com"

def show_posts(limit=15):
    request = requests.get(f'{url}/posts?limit={limit}',params = {'_limit' : limit})
    request.raise_for_status()
    post = request.json()

    print(f'First: {len(post)} posts')
    for post in post:
        print(f'{post['id']}: {post["title"]}')

    return


def get_title(post_id):
    response = requests.get(f'{url}/posts/{post_id}')
    response.raise_for_status()
    post = response.json()
    return post['title']


def create_post(title,body,userId=8):
    new_post = { 'title': title , 'body': body,'user_id': userId}
    response = requests.post(f'{url}/posts',json = new_post,)
    response.raise_for_status()
    return response.status_code, response.json()


def get_post(post_id):
    post = requests.get(f'{url}/posts/{post_id}')
    try:
        print("\n\nType in the id of the post up to 100 \nFor example...")
        print(f'\nThis is post : {post.json()['title']} : id number {str(post_id)}')
        choice = input('Enter it here: ')
        post = requests.get(f'{url}/posts/{choice}')
        print(f'\nThis is JSON body : {post.json()['body']} : id number {str(choice)}')
    except requests.RequestException as error:
        print('error...')
    return post.json()

def main():
    try:
        show_posts(limit = 15)
        print(get_title(4))
        status_code, created_post = create_post(title = "This is a title I made",body = 'This is the body', userId = 777)
        print('\n Post response: ')
        print(f'status_code: {status_code}')
        print(f'created_post: {created_post}')
        get_post(5)

    except requests.RequestException as error:
        print(error)


if __name__ == "__main__":
    main()

