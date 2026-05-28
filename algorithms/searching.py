def linear_search(linkedlist, target):
    now = linkedlist.head

    while now:
        if now.data.nama.lower() == target.lower():
            return now.data
        
        now = now.next
    return None