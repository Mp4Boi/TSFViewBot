import requests
#import time

def MethodViews():
    url = "https://topstreetfights.com/wp-admin/admin-ajax.php?td_theme_name=Newsmag&v=5.2.1"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Alt-Used": "topstreetfights.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    
    if not hasattr(MethodViews, 'post_id'):
        MethodViews.post_id = input("Please enter a post ID (Read Help.txt if you don't know how to get it)")
    
    data = {
        "action": "td_ajax_update_views",
        "td_post_ids": f"[{MethodViews.post_id}]"
    }
    
    response = requests.post(url, headers=headers, data=data)
    print("Sent Views!")
    #time.sleep(0.1)
    MethodViews()

MethodViews()
