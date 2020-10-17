1. 清除浮动overflow: hidden;
2. 元素居中 
	position:absolute
	left:50% 
	top:50% 
	transform:translate(-50%,-50%)
	
	display:flex
	align-items:center
3. mutation-commit action-dispath
4.  父传子 props
	字传父 this.$emit()
	兄弟  eventBus.$emit('todo',this.name) eventBus.$on('todo',function(data){ })  eventBus.$off('todo'）
	主动获取：refs
5. 路由拦截，全局守卫router.beforeEach axios.interceptors.response.use(response=>{})