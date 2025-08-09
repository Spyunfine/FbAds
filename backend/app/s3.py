from minio import Minio
from .config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET

_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)

def ensure_bucket():
    found = _client.bucket_exists(MINIO_BUCKET)
    if not found:
        _client.make_bucket(MINIO_BUCKET)

def presigned_get(key: str, expires=3600) -> str:
    return _client.presigned_get_object(MINIO_BUCKET, key, expires=expires)

def put_object(key: str, data: bytes, content_type: str):
    from io import BytesIO
    _client.put_object(MINIO_BUCKET, key, BytesIO(data), len(data), content_type=content_type)
