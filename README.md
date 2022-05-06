# JFC

### Jina Flow Companion

That's right: Jina Flow Companion. Not Jentucky Fried Chicken, or Jesus Fiona Christ.

## What do it do?

A simple CLI to:

- Index data from a folder, file, text string, CSV, or (coming soon) DocArray on Jina Cloud
- Search data via string or file

## Features

- Read config from YAML or command-line arguments
- Connect via REST, gRPC, or WebSockets gateways
- (Coming soon) incremental indexing - only index new data

### Install

This will be implemented soon:

```
pip install jfc
```

### Index

```
jfc index -d <name_of_folder>/<csv_filename>
```

### Search

```
jfc search -d <string>/<image.png>
```

### Arguments

| Argument | Meaning                                            | 
| ---      | ---                                                | 
| `-h`     | URL to host                                        | 
| `-d`     | Path to data source                                | 
| `-n`     | Number of documents to index OR return from search |
| `-c`     | Load all arguments from YAML file                  |
