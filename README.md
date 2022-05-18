# JFC

### Jina Flow Companion

That's right: Jina Flow Companion. Not Jentucky Fried Chicken, or Jesus Fiona Christ.

## What do it do?

A simple CLI to:

- Index data from a folder, file, text string, CSV, or (coming soon) DocArray on Jina Cloud
- Search data via string or file

## Features

- Read config from YAML (coming soon) or command-line arguments
- Connect via REST, gRPC, or WebSockets gateways

### Install

This will be implemented soon:

```
pip install jfc
```

### Index

```
jfc index <data>
```

Where `<data` is a CSV file or glob

### Search

```
jfc search <data>
```

Where <data> is a file or string

### Arguments

| Argument | Meaning                                            | 
| ---      | ---                                                | 
| `-h`     | URL to host                                        | 
| `-n`     | Number of documents to index OR return from search |
