# Spec 

This file defines how to write an extension compatible with lyra

An extension consists of 2 files

The core script that will be loaded and eun by lyra

```
<extension>.py
```

and 

A file to define metadata about the extension, this will allow lyra to check for extension updates 
and show the user information about the extension

```
manifest.json
```

#### extension.py

This is the core scraper script, based on the type of media you want to scrape you must implement each 
methods defined in the sections below

**Note: Currently only manga methods are supported**

##### Manga extension

To implement a manga extension you must add the following top level functions in your python script

get_book_metadata

 TODO

#### manifest.json

You must also add this file this is what lyra will use to manage the extension

The following fields will be required

```json
{
  "name": "test extension",
  "manifest_version": 1,
  "version": "0.0.1",
  "media_type": "manga",
  "repoUrl": "https://github.com/RA341/test_scripts",
  "scriptUrl": "https://raw.githubusercontent.com/RA341/test_scripts/main/test.py",
  "metaDataUrl": "https://raw.githubusercontent.com/RA341/test_scripts/main/test_extension.json"
}
```