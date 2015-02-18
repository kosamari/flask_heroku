from boto.s3.connection import S3Connection
from boto.s3.key import Key
conn = S3Connection(os.environ.get('AWS_ACCESS_KEY_ID'),os.environ.get('AWS_SECRET_ACCESS_KEY'))
bucket = conn.get_bucket(os.environ.get('S3_BUCKET'))
k = Key(bucket)
k.key = 'key_name'
k.set_contents_from_string('contents')
k.get_contents_as_string()
