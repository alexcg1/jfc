from jina import Client
from docarray import DocumentArray, Document
import os
from helper import preproc, load_config, Formats, default_config
import click
import sys


def index(host, num_docs, data, config_file=None, **kwargs):
    if config_file:
        config = load_config(config_file)
    else:
        config = default_config

    if host:
        config["host"] = host
    if num_docs:
        config["indexing"]["num_docs"] = int(num_docs)
    if data:
        config["indexing"]["data"] = data


    if not host:
        print("Please specify a host")
        sys.exit()

    # if not os.path.isfile(config["indexing"]["db_name"]):
        # print("Running for first time, creating initial database")

    # All the already indexed files
    # already_indexed = DocumentArray(
    # storage="sqlite", config={"connection": config["indexing"]["db_name"], "table_name": "docs"}
    # )

    # All docs in the data dir - indexed already, and un-indexed
    # all_docs = DocumentArray.from_files(
    # config["indexing"]["data"], recursive=True, size=int(num_docs)
    # )

    # new_docs = DocumentArray()
    # for doc in all_docs:
    # if doc.uri not in already_indexed[:, "uri"]:
    # print(f"{doc.uri} not indexed yet")
    # new_docs.append(doc)
    # else:
    # print(f"{doc.uri} already indexed")

    if os.path.isdir(data):
        print(f"Indexing from folder: {data}")
        # indexing_type = "folder"
        # all_docs = DocumentArray.from_files(f"{data}/**/*.jpg", recursive=True, size=int(num_docs)) # fix this to use all image formats
        docs = DocumentArray.from_files(
            f"{config['indexing']['data']}/**/*.jpg",
            recursive=True,
            size=int(config["indexing"]["num_docs"]),
        )  # fix this to use all image formats
        # for doc in all_docs:
            # if doc.uri not in already_indexed[:, "uri"]:
                # print(f"{doc.uri} not indexed yet")
                # new_docs.append(doc)
            # else:
                # print(f"{doc.uri} already indexed")

    elif os.path.isfile(data) and data.split(".")[-1] in Formats.table:
        # print("Indexing from csv")
        # indexing_type = "table"
        docs = DocumentArray.from_csv(data)
        # all_docs.summary()
        docs.summary()

    else:
        print("Unrecognized data")

    # for doc in all_docs:
    # if doc.uri not in already_indexed[:, "uri"]:
    # print(f"{doc.uri} not indexed yet")
    # new_docs.append(doc)
    # else:
    # print(f"{doc.uri} already indexed")

    # Now we'll use the client to send only the new docs to our indexing Flow
    # for doc in new_docs:
    for doc in docs:
        if doc.uri:
            print(f"Processing {doc.uri}")
            preproc(doc)

    # new_docs.summary()
    client = Client(host=config["host"])
    client.index(docs)
    # client.index(new_docs)

    # Extend our already indexed docs to reflect what's been indexed
    # already_indexed.extend(new_docs)


def search(data, host, config=None, **kwargs):
    if config:
        config = load_config(config)
    if os.path.isfile(data) and data.split(".")[-1] in Formats.image:
        search_type = "image"
        doc = Document(uri=data)
        print(f"Searching with image {doc.uri}")
        preproc(doc)

    elif os.path.isfile(data) and data.split(".")[-1] in Formats.table:
        search_type = "table"
        pass

    else:
        # assume it's a string
        search_type = "text"
        doc = Document(text=data)

    client = Client(host=host)
    response = client.search(doc)

    for match in response[0].matches:
        if search_type == "text":
            print(match.text)
        else:
            print(match.uri)


# index()
# search("data/images/10000.jpg")


@click.command()
@click.argument("task")
@click.option("--num_docs", "-n")
@click.option("--data", "-d")
@click.option("--host", "-h")
@click.option("--config_file", "-c")
def main(task: str, host, num_docs, data, config_file):
    if task == "index":
        index(config_file=config_file, host=host, num_docs=num_docs, data=data)
    elif task == "search":
        search(config, data)
    else:
        print("Please add 'index' or 'search' to your command")


if __name__ == "__main__":
    main()
