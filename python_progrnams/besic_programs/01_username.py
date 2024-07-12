if __name__ == "__main__":
    username:str = input("Enter username (min 3 char): ")
    if len(username)>=3:
        print(f'Hello {username}, How are you?')
    else:
        print(f'Error: {username} is lase than 3 character')