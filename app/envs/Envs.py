from decouple import config

linode_access_key = config('LINODE_ACCESS_KEY')
linode_secret_key = config('LINODE_SECRET_KEY')
linode_endpoint_url = config('LINODE_ENDPOINT_URL')
bucket_label = config('BUCKET_LABEL')
region_name = config('REGION_NAME')