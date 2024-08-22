# import datetime
# from google.cloud import storage

# def list_buckets(project_id):
#     """Lists all buckets in a given project."""
#     storage_client = storage.Client(project=project_id)
#     return list(storage_client.list_buckets())  # Convert to list

# def write_to_gcs(bucket_name, filename, content):
#     """Writes content to a file in a GCS bucket."""
#     print(content)
#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(filename)
#     blob.upload_from_string(content)

# def main():
#     project_id = "pkdeltaai-06"
#     bucket_name = "bkt-pkdeltaai-06-uc1"

#     buckets = list_buckets(project_id)

#     # Ensure each bucket name is on a new line, even if there's only one
#     output_data = "\n".join([bucket.name for bucket in buckets]) + "\n"
#     filename = f"output-{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"
#     print(output_data)

#     write_to_gcs(bucket_name, filename, output_data)

# if __name__ == "__main__":
#     main()



import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


