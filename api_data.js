define({ "api": [  {    "type": "post",    "url": "/user/article/",    "title": "Create a article",    "name": "Create_a_article",    "group": "Article",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "title",            "description": "<p>The article title.</p>"          },          {            "group": "Parameter",            "type": "Json",            "optional": false,            "field": "tags",            "description": "<p>The user custom tags.</p>"          }        ]      },      "examples": [        {          "title": "Request (Example):",          "content": "{\n    \"title\": \"God know what it is\",\n    \"list_id\": \"aldkfjdaslkfjl\",\n    \"description\": \"I don't know\",\n    \"url\": \"https://www.gooel.com/something\",\n    \"tags\": [\"tag1\", \"tag2\", \"tag3\"]\n}",          "type": "json"        }      ]    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "Message",            "description": "<p>Success message.</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "app/api/article/controller.py",    "groupTitle": "Article",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        },        {          "title": "Error 400",          "content": "{\n    \"msg\": \"List does not exist\"\n}",          "type": "json"        }      ]    }  },  {    "type": "post",    "url": "/user/article/",    "title": "Create a article",    "name": "Create_a_article",    "group": "Article",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "title",            "description": "<p>The article title.</p>"          },          {            "group": "Parameter",            "type": "Json",            "optional": false,            "field": "tags",            "description": "<p>The user custom tags.</p>"          }        ]      },      "examples": [        {          "title": "Request (Example):",          "content": "{\n    \"tag\": \"science\"\n}",          "type": "json"        }      ]    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "Message",            "description": "<p>Success message.</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "app/api/article/controller.py",    "groupTitle": "Article",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        },        {          "title": "Error 400",          "content": "{\n    \"msg\": \"List does not exist\"\n}",          "type": "json"        }      ]    }  },  {    "type": "get",    "url": "/user/article/:id",    "title": "Get a article",    "name": "Get_a_article",    "group": "Article",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Article unique ID.</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Article id.</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "title",            "description": "<p>Article title.</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "list_id",            "description": "<p>List id.</p>"          },          {            "group": "Success 200",            "type": "Object[]",            "optional": false,            "field": "comments",            "description": "<p>User comments.</p>"          },          {            "group": "Success 200",            "type": "Object",            "optional": false,            "field": "comments.content",            "description": "<p>The content.</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "comments.timestamp",            "description": "<p>The timestamp of the comment.</p>"          }        ]      },      "examples": [        {          "title": "Response (Example):",          "content": "{\n    \"id\": \"aldkfjadls\",\n    \"title\": \"Process\",\n    \"description\": \"adlsfjdlask\",\n    \"url\": \"https://www.google.com/something\",\n    \"list_id\": \"ladsjflas\",\n    \"comments\" : [{\n        \"id\": \"afjlkdsfjafla\",\n        \"content\": \"i hate it\",\n        \"timestamp\": \"2017-02-04-19-59-59\"\n    }],\n    \"tags\": [\"science\", \"computer\"]\n}",          "type": "json"        }      ]    },    "version": "0.0.0",    "filename": "app/api/article/controller.py",    "groupTitle": "Article",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        }      ]    }  },  {    "type": "get",    "url": "/user/article/:id/comment",    "title": "Post comment to an article",    "name": "Post_comment_to_an_article",    "group": "Article",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>Article unique ID.</p>"          },          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "comment",            "description": "<p>The comment to be added</p>"          },          {            "group": "Parameter",            "type": "Boolean",            "optional": false,            "field": "public",            "description": "<p>The privacy setting for the comment, default is True</p>"          }        ]      },      "examples": [        {          "title": "Request (Example)",          "content": "{\n    \"comment\": \"I hate you\",\n    \"public\": \"false\"\n}",          "type": "json"        }      ]    },    "version": "0.0.0",    "filename": "app/api/comment/controller.py",    "groupTitle": "Article",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        },        {          "title": "Error 400",          "content": "{\n    \"msg\": \"Article does not exist\"\n}",          "type": "json"        }      ]    }  },  {    "type": "delete",    "url": "/user/list/:list_id",    "title": "Archive a list",    "name": "Archive_a_list",    "group": "List",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "list_id",            "description": "<p>The list id.</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>User id</p>"          },          {            "group": "Success 200",            "type": "Object[]",            "optional": false,            "field": "lists",            "description": "<p>Lists data</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "lists.id",            "description": "<p>List id</p>"          },          {            "group": "Success 200",            "type": "Boolean",            "optional": false,            "field": "lists.archived",            "description": "<p>Archived list or not</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "lists.name",            "description": "<p>List name</p>"          }        ]      },      "examples": [        {          "title": "Response (Example):",          "content": "{\n    \"id\": \"31ladsjfl\",\n    \"lists\": [\n        {\n            \"id\": \"adlfajdls\",\n            \"archived\": \"True\",\n            \"name\": \"Process\"\n        }\n    ]\n}",          "type": "json"        }      ]    },    "version": "0.0.0",    "filename": "app/api/list/controller.py",    "groupTitle": "List",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        },        {          "title": "Error 400",          "content": "{\n    \"msg\": \"List does not exist\"\n}",          "type": "json"        }      ]    }  },  {    "type": "get",    "url": "/user/list",    "title": "Create a reading list",    "name": "Create_a_reading_list",    "group": "List",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "name",            "description": "<p>List name.</p>"          }        ]      },      "examples": [        {          "title": "Request (Example)",          "content": "{\n    \"name\": \"CMPUT495 Seminar\"\n}",          "type": "json"        }      ]    },    "version": "0.0.0",    "filename": "app/api/list/controller.py",    "groupTitle": "List",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        }      ]    }  },  {    "type": "delete",    "url": "/user/list/:list_id/article/:article_id",    "title": "Delete an article",    "name": "Delete_an_article_from_a_list",    "group": "List",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "list_id",            "description": "<p>The list id.</p>"          },          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "article_id",            "description": "<p>The article id.</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "JSON",            "optional": false,            "field": "List",            "description": "<p>the new list in json string.</p>"          }        ]      }    },    "version": "0.0.0",    "filename": "app/api/list/controller.py",    "groupTitle": "List",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        },        {          "title": "Error 400",          "content": "{\n    \"msg\": \"List does not exist\"\n}",          "type": "json"        },        {          "title": "Error 400",          "content": "{\n    \"msg\": \"Article does not exist\"\n}",          "type": "json"        }      ]    }  },  {    "type": "get",    "url": "/user/list/:id",    "title": "Get articles of a list",    "name": "Get_articles_of_a_list",    "group": "List",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>List unique ID.</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "List",            "description": "<p>id.</p>"          },          {            "group": "Success 200",            "type": "Object[]",            "optional": false,            "field": "articles",            "description": "<p>Articles data.</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "articles.id",            "description": "<p>Article id.</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "article.title",            "description": "<p>Article title.</p>"          }        ]      },      "examples": [        {          "title": "Response (Example):",          "content": "{\n    \"id\": \"31ladsjfl\",\n    \"name\": \"CMPUT 391 Seminar\",\n    \"articles\": [\n        {\n            \"id\": \"adlfajdls\",\n            \"title\": \"Process\"\n        }\n    ]\n}",          "type": "json"        }      ]    },    "version": "0.0.0",    "filename": "app/api/list/controller.py",    "groupTitle": "List",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        }      ]    }  },  {    "type": "get",    "url": "/user/lists",    "title": "Get user all reading lists",    "name": "Get_user_reading_lists",    "group": "List",    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>User id</p>"          },          {            "group": "Success 200",            "type": "Object[]",            "optional": false,            "field": "lists",            "description": "<p>Lists data</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "lists.id",            "description": "<p>List id</p>"          },          {            "group": "Success 200",            "type": "Boolean",            "optional": false,            "field": "lists.archived",            "description": "<p>Archived list or not</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "lists.name",            "description": "<p>List name</p>"          }        ]      },      "examples": [        {          "title": "Response (Example):",          "content": "{\n    \"id\": \"31ladsjfl\",\n    \"lists\": [\n        {\n            \"id\": \"adlfajdls\",\n            \"archived\": \"True\",\n            \"name\": \"Process\"\n        }\n    ]\n}",          "type": "json"        }      ]    },    "version": "0.0.0",    "filename": "app/api/list/controller.py",    "groupTitle": "List",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        }      ]    }  },  {    "type": "put",    "url": "/user/list/:list_id",    "title": "Retrieve a list",    "name": "Retrieve_a_list",    "group": "List",    "parameter": {      "fields": {        "Parameter": [          {            "group": "Parameter",            "type": "String",            "optional": false,            "field": "list_id",            "description": "<p>The list id.</p>"          }        ]      }    },    "success": {      "fields": {        "Success 200": [          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "id",            "description": "<p>User id</p>"          },          {            "group": "Success 200",            "type": "Object[]",            "optional": false,            "field": "lists",            "description": "<p>Lists data</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "lists.id",            "description": "<p>List id</p>"          },          {            "group": "Success 200",            "type": "Boolean",            "optional": false,            "field": "lists.archived",            "description": "<p>Archived list or not</p>"          },          {            "group": "Success 200",            "type": "String",            "optional": false,            "field": "lists.name",            "description": "<p>List name</p>"          }        ]      },      "examples": [        {          "title": "Response (Example):",          "content": "{\n    \"id\": \"31ladsjfl\",\n    \"lists\": [\n        {\n            \"id\": \"adlfajdls\",\n            \"archived\": \"False\",\n            \"name\": \"Process\"\n        }\n    ]\n}",          "type": "json"        }      ]    },    "version": "0.0.0",    "filename": "app/api/list/controller.py",    "groupTitle": "List",    "header": {      "fields": {        "Header": [          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Access-Token",            "description": "<p>Access token obtains from Oauth2 provider.</p>"          },          {            "group": "Header",            "type": "String",            "optional": false,            "field": "Provider-Name",            "description": "<p>Oauth2 provider name.</p>"          }        ]      },      "examples": [        {          "title": "Header (Example):",          "content": "{\n    \"Access-Token\": \"12xsdklajlkadsf\",\n    \"Provider-Name\": \"Google\"\n}",          "type": "json"        }      ]    },    "error": {      "fields": {        "Error 4xx": [          {            "group": "Error 4xx",            "optional": false,            "field": "UnauthorizedAccessError",            "description": "<p>User's access token is not valid</p>"          }        ]      },      "examples": [        {          "title": "Error 401",          "content": "{\n    \"msg\": \"Unauthorized access\"\n}",          "type": "json"        },        {          "title": "Error 400",          "content": "{\n    \"msg\": \"List does not exist\"\n}",          "type": "json"        }      ]    }  }] });
