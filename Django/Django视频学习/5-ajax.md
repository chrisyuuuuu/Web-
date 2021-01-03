# ajax
	- 页面不刷新的情况下，偷偷请求后台
	```
		<input onclick="AjaxSend"><span id="errormessage"><>
		function AjaxSend(){
			$.ajax({
				url:'//',
				method:'POST',
				data:{'title':$('#title').val()},
				success:fucntion(data){
					//当服务器处理完成后，返回数据时，该函数自动调用
					//data = 服务器返回的值
					if(data=="ok"){
						...
						location.url='//'
					}else{
						$('#errormessage').text(data)
					}
				}
			})
		}
	```
	- ajax只能返回字符串，不能跳转网址，想跳转+js
	- 引入jQuery
	- $.ajax({
		url:'',
		type:'',
		data:{},
		success:function(data){
			
		}
	})
	-  Ajax提交页面不会刷新，Form表单会刷新
	- onclick return  false 结束跳转
	```
		var v = $(ths).parent().prevAll()
	
	```
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	