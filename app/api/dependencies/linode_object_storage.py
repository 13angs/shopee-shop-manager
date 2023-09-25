from app.envs import Envs
import boto3
import os
import uuid
import shutil
from app.api.dependencies.pdf_merge import merge_all_pdfs

linode_obj_config = {
    "aws_access_key_id": Envs.linode_access_key,
    "aws_secret_access_key": Envs.linode_secret_key,
    "endpoint_url": Envs.linode_endpoint_url,
}

client = boto3.client("s3", **linode_obj_config)


def download_pdf(filename: str, sub_dir: str = ''):
    # data + sub_dir + filename
    full_path = os.path.join('data', sub_dir, filename)

    # get the sub_dir path
    sub_dir_path = os.path.join('data', sub_dir)

    # check if the sub_dir exist
    existing_dir = os.path.isdir(sub_dir_path)

    # if sub_dir not exist and
    # sub_dir is specified
    # create the sub_dir
    if len(sub_dir) > 0 and existing_dir == False:
        os.mkdir(sub_dir_path)

    # get the the full path from object storage
    key = os.path.join('invoices', filename)

    try:
        # start downloading the file
        client.download_file(
            Bucket=Envs.bucket_label,
            Key=key,
            Filename=full_path)
    except Exception as e:
        print(f'{key} not found')
        print(e)


def download_pdfs(order_sn: list):

    # if order_sn is equal to 0 return immediately
    if len(order_sn) == 0:
        return

    # generate the sub_dir using guid
    sub_dir = str(uuid.uuid1())

    # loop throght each one of order_sn
    # process or download the pdf one by one
    for filename in order_sn:
        download_pdf(filename, sub_dir)

    print('Finished dowloading pdfs')

    # get the sub_dir full path
    sub_dir_path = os.path.join('data', sub_dir)

    # get the full pdf file path
    pdf_files = []
    for file in order_sn:
        pdf_files.append(
            os.path.join(sub_dir_path, file)
        )

    # start merging the pdfs
    merged_pdf_name, merged_pdf_path = merge_all_pdfs(sub_dir_path, pdf_files)

    # get the destination path
    dest_path = os.path.join('invoices', merged_pdf_name)
    upload_file(merged_pdf_path, dest_path)

    # get the presigned url
    url = get_presigned_url(dest_path)

    # # rest for 2 secs
    # time.sleep(2)

    # delete the sub_dir and its contents
    shutil.rmtree(sub_dir_path)
    print('All pdfs removed!')

    return url


def upload_file(file_path: str, dest_path: str):
    client.upload_file(
        Filename=file_path,
        Bucket=Envs.bucket_label,
        Key=dest_path
    )

def get_presigned_url(object_key: str, expire: int = 3600):

    url = client.generate_presigned_url(
        'get_object',  # The S3 operation to allow (e.g., 'get_object' to download)
        Params={'Bucket': Envs.bucket_label, 'Key': object_key},
        ExpiresIn=expire
    )

    print("Generated URL:", url)
    return url

