from google.cloud import storage

def get_the_risk(request):
    client = storage.Client()
    to_res = []
    for bucket in client.list_buckets():
        to_res.append(str(bucket))
    return to_res
