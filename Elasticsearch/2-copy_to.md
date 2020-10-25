PUT myindex2
{
  "mappings": {
    "xxxxxxxxxxxxxxxx":{
      "dynamic":false,
      "properties":
          {
            "name":{
              "type":"text",
              "copy_to":"fullname"
            },
            "age":{
              "type":"long",
              "copy_to":"fullname"
            },
            "fullname":{
              "type":"text"
            }
          }
    }
  }
}

PUT myindex2/xxxxxxxxxxxxxxxx/1
{
  "name":"aaa",
  "age":10
}
PUT myindex2/xxxxxxxxxxxxxxxx/2
{
  "name":"bbb",
  "age":100
}
GET /myindex2/xxxxxxxxxxxxxxxx/_search
{
  "query": {
    "match": {
      "fullname": "aaa"
    }
  }
}
返回结果：
	{
	  "took" : 1,
	  "timed_out" : false,
	  "_shards" : {
		"total" : 5,
		"successful" : 5,
		"skipped" : 0,
		"failed" : 0
	  },
	  "hits" : {
		"total" : 1,
		"max_score" : 0.2876821,
		"hits" : [
		  {
			"_index" : "myindex2",
			"_type" : "xxxxxxxxxxxxxxxx",
			"_id" : "1",
			"_score" : 0.2876821,
			"_source" : {
			  "name" : "aaa",
			  "age" : 10
			}
		  }
		]
	  }
	}
# 注意：copy_to 参数，当前字段复制给指定字段，
# index参数：是否为它创建索引，默认True