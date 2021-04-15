#GitPy
___
###GitPy is a python module/REST-API for working with different source code management software(Git, Mercurial, SVN, etc...)

## INSTALLATION
___
`create environment: https://docs.python.org/3/library/venv.html` <br>
`install requirements: pip insatll -r requirements.txt` <br>
`run server: python app.py`
##REST API

**Last Commit**
----
  Returns json data about a last commit in repository.

* **URL**

  /last_commit/

* **Method:**

  `GET`
  
*  **URL Params**

    None
   **Required:**
 
* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
      {
      "author":{...},
      "comments_url":"https://api.github.com/repos/ArtakNiazyan/gitpy/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc/comments",
      "commit":{
         "author":{...},
         "comment_count":0,
         "committer":{...},
         "message":"fix webhook api response",
         "tree":{
            "sha":"53a5b7e292e99e27585db32f1ff545b3ec8ea7ae",
            "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/git/trees/53a5b7e292e99e27585db32f1ff545b3ec8ea7ae"
         },
         "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/git/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
         "verification":{...}
      },
      "committer":{...},
      "files":[{...}],
      "html_url":"https://github.com/ArtakNiazyan/gitpy/commit/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
      "node_id":"MDY6Q29tbWl0MzU3MjcyODc1OmE5YzgxYWI3ODgwZjhmZmNkNDQzZWQxNGY3YzQ4YmIwNmM2MjJjZmM=",
      "parents":[{...}],
      "sha":"a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
      "stats":{...},
      "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc"
   }
    `
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"data": "Commit not found", "status": 404}`


**Last Commit**
----
  Returns json data about a last commit in repository.

* **URL**

  /get_commit/<str:commit_hash>/

* **Method:**

  `GET`
  
*  **URL Params**
 
   **Required:**
   
    commit_hash=string
 

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
      {
      "author":{...},
      "comments_url":"https://api.github.com/repos/ArtakNiazyan/gitpy/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc/comments",
      "commit":{
         "author":{...},
         "comment_count":0,
         "committer":{...},
         "message":"fix webhook api response",
         "tree":{
            "sha":"53a5b7e292e99e27585db32f1ff545b3ec8ea7ae",
            "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/git/trees/53a5b7e292e99e27585db32f1ff545b3ec8ea7ae"
         },
         "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/git/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
         "verification":{...}
      },
      "committer":{...},
      "files":[{...}],
      "html_url":"https://github.com/ArtakNiazyan/gitpy/commit/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
      "node_id":"MDY6Q29tbWl0MzU3MjcyODc1OmE5YzgxYWI3ODgwZjhmZmNkNDQzZWQxNGY3YzQ4YmIwNmM2MjJjZmM=",
      "parents":[{...}],
      "sha":"a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
      "stats":{...},
      "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc"
   }
    `
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"data": "Commit not found", "status": 404}`


**Last Commit**
----
  Returns json data about a commit with given sha.

* **URL**

  /last_commit/<str:commit_hash>/

* **Method:**

  `GET`
  
*  **URL Params**
 
   **Required:**
   
    commit_hash=string
 

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
      {
      "author":{...},
      "comments_url":"https://api.github.com/repos/ArtakNiazyan/gitpy/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc/comments",
      "commit":{
         "author":{...},
         "comment_count":0,
         "committer":{...},
         "message":"fix webhook api response",
         "tree":{
            "sha":"53a5b7e292e99e27585db32f1ff545b3ec8ea7ae",
            "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/git/trees/53a5b7e292e99e27585db32f1ff545b3ec8ea7ae"
         },
         "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/git/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
         "verification":{...}
      },
      "committer":{...},
      "files":[{...}],
      "html_url":"https://github.com/ArtakNiazyan/gitpy/commit/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
      "node_id":"MDY6Q29tbWl0MzU3MjcyODc1OmE5YzgxYWI3ODgwZjhmZmNkNDQzZWQxNGY3YzQ4YmIwNmM2MjJjZmM=",
      "parents":[{...}],
      "sha":"a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
      "stats":{...},
      "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc"
   }
    `
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"data": "Commit not found", "status": 404}`



**Parent Commit**
----
  Returns json data about a parent commit of the given one.

* **URL**

  /get_parent/<str:commit_hash>/

* **Method:**

  `GET`
  
*  **URL Params**
 
   **Required:**
   
    commit_hash=string
 

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
      {
      "author":{...},
      "comments_url":"https://api.github.com/repos/ArtakNiazyan/gitpy/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc/comments",
      "commit":{
         "author":{...},
         "comment_count":0,
         "committer":{...},
         "message":"fix webhook api response",
         "tree":{
            "sha":"53a5b7e292e99e27585db32f1ff545b3ec8ea7ae",
            "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/git/trees/53a5b7e292e99e27585db32f1ff545b3ec8ea7ae"
         },
         "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/git/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
         "verification":{...}
      },
      "committer":{...},
      "files":[{...}],
      "html_url":"https://github.com/ArtakNiazyan/gitpy/commit/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
      "node_id":"MDY6Q29tbWl0MzU3MjcyODc1OmE5YzgxYWI3ODgwZjhmZmNkNDQzZWQxNGY3YzQ4YmIwNmM2MjJjZmM=",
      "parents":[{...}],
      "sha":"a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
      "stats":{...},
      "url":"https://api.github.com/repos/ArtakNiazyan/gitpy/commits/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc"
   }
    `
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"data": "Commit not found", "status": 404}`


**Committed Files**
----
  Returns json data about files from commit of.

* **URL**

  /get_files/<str:commit_hash>/

* **Method:**

  `GET`
  
*  **URL Params**
 
   **Required:**
   
    commit_hash=string
 

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
      {
         "additions":4,
         "blob_url":"https://github.com/ArtakNiazyan/gitpy/blob/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc/app.py",
         "changes":9,
         "contents_url":"https://api.github.com/repos/ArtakNiazyan/gitpy/contents/app.py?ref=a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc",
         "deletions":5,
         "filename":"app.py",
         "patch":"@@ -6,9 +6,6 @@\n \n app = Flask(__name__)\n \n-app.branch_logger = configure_log_file(\"branch_logs\")\n-app.commit_logger = configure_log_file(\"commits_logs\")\n-\n \n @app.route('/last_commit/')\n def last_commit():\n@@ -59,16 +56,18 @@ def get_file_content():\n def branch_created():\n     request_data = request.get_json()\n     app.branch_logger.info(request_data)\n-    return 200\n+    return jsonify({\"status\": 200})\n \n \n @app.route('/commit-pushed', methods=['POST'])\n def commit_created():\n     request_data = request.get_json()\n     app.commit_logger.info(request_data)\n-    return 200\n+    return jsonify({\"status\": 200})\n \n \n if __name__ == '__main__':\n     app.vc_manager = vc_manager\n+    app.branch_logger = configure_log_file(\"branch_logs\")\n+    app.commit_logger = configure_log_file(\"commits_logs\")\n     app.run()",
         "raw_url":"https://github.com/ArtakNiazyan/gitpy/raw/a9c81ab7880f8ffcd443ed14f7c48bb06c622cfc/app.py",
         "sha":"8d21ed883f5b124d113cd838de1fd84fc948e530",
         "status":"modified"
      }
    `
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"data": "Commit not found", "status": 404}`


**Files Content**
----
  Returns json data with file content.

* **URL**

  /get_file_content/

* **Method:**

  `GET`
  
*  **URL Params**

  None

* **Data Params**

    filename=string


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `
      {
         "data":"from flask import Flask, request, jsonify\n\nfrom exceptions import CommitNotFound, FileNotFound\nfrom utils import configure_log_file\nfrom vc_service import vc_manager\n\napp = Flask(__name__)\n\n\n@app.route('/last_commit/')\ndef last_commit():\n    \"\"\"API view for getting last commit in the repository\"\"\"\n    try:\n        commit_data = app.vc_manager.last_commit()\n        resp = jsonify({\"data\": commit_data, \"status\": 200})\n    except CommitNotFound:\n        resp = jsonify({\"data\": \"Commit not found\", \"status\": 404})\n    return resp\n\n\n@app.route('/parent_commit/<commit_hash>/')\ndef parent_commit(commit_hash):\n    \"\"\"API view for getting next commit right after given one\"\"\"\n    try:\n        commit = app.vc_manager.get_parent_commit(commit_hash)\n        resp = jsonify({\"data\": commit.raw_data, \"status\": 200})\n    except CommitNotFound:\n        resp = jsonify({\"data\": \"Commit Not Found\", \"status\": 404})\n    return resp\n\n\n@app.route('/get_files/<commit_hash>/')\ndef get_files(commit_hash):\n    \"\"\"API view for getting files from commit\"\"\"\n    try:\n        files = app.vc_manager.get_files_from_commit(commit_hash)\n        resp = jsonify({\"data\": files, \"status\": 200})\n    except CommitNotFound:\n        resp = jsonify({\"data\": \"Commit not found\", \"status\": 404})\n    return resp\n\n\n@app.route('/get_file_content/')\ndef get_file_content():\n    \"\"\"API view for getting file content\"\"\"\n    filename = request.args.get(\"filename\")\n    try:\n        file_content = app.vc_manager.get_file_content(filename)\n        resp = jsonify({\"data\": file_content, \"status\": 200})\n    except FileNotFound:\n        resp = jsonify({\"data\": \"File not found\", \"status\": 404})\n    return resp\n\n\n@app.route('/branch-created', methods=['POST'])\ndef branch_created():\n    request_data = request.get_json()\n    app.branch_logger.info(request_data)\n    return jsonify({\"status\": 200})\n\n\n@app.route('/commit-pushed', methods=['POST'])\ndef commit_created():\n    request_data = request.get_json()\n    app.commit_logger.info(request_data)\n    return jsonify({\"status\": 200})\n\n\nif __name__ == '__main__':\n    app.vc_manager = vc_manager\n    app.branch_logger = configure_log_file(\"branch_logs\")\n    app.commit_logger = configure_log_file(\"commits_logs\")\n    app.run()\n",
      }
    `
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{"data": "File found", "status": 404}`


##Webhooks

**Branches created/deleted**
----
  Whebhook listeners receives events about branch creation/deletion and writes in log file.

* **URL**

  /branch_created

* **Method:**

  `POST`
  
*  **URL Params**

    None

* **Data Params**

    None

**Commit pushed**
----
  Whebhook listeners receives commit pushes and writes in log file.

* **URL**

  /commit_pushed

* **Method:**

   `POST`
  
*  **URL Params**

    None

* **Data Params**

    None
