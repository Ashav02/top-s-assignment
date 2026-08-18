#'user_status' and 'app_status'

app_status = "offline"

print("before function:", app_status)

def update_status():
    user_status = "online"
    print("inside function:", user_status)

update_status()

print("after function:", app_status)