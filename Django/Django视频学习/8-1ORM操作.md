```
def __str__(self)
	return self.name
用于查看：querySet对象可以转为self.name	


排序
filter().order_by('id','name')

分组 
models.UserInfo.objects.values("ut_id') select ut_id form UserInfo
import Count,Sum,Max,Min
v = models.UserInfo.objects.values("ut_id').annotate(xxx=Count('id')) 
v = select ut_id,count(id) form UserInfo group by id
分组后二次删选 filter在前表示where后表示having
v = models.UserInfo.objects.values("ut_id').annotate(xxxx=Count('id')).filter(xxxx__gt=2)
 __gt
 __in
 __range
 __startwith
 __endwith	
 __contains
 不等于
 exclude(id=1) <----> id!=1


v.query(查看生成的sql语句)

### F,Q F("age"):获取原来的值
update User set username = '11' where id=1;
all().update(age=F("age")+1)

###Q对象 、Q方法解决or的问题  构造复杂的查询条件
运用1：filter(Q(id=1) | Q(name="alice") & Q(id=12))
运用2
q2  = Q()
q2.connector = 'OR'
q2.children.append(('c1',1))

con = Q()

con.add(q1,'AND')
con.add(q2,'AND')

filter(con)




select id,
		(select count(1) from tb) as n
	from xb
all().extra(select={'n':"selct count(n) from xxx where id = %s"},
	select_params = [1]
	)
filter().extra(
	where = ["id=1 or id=2 ","name='asd'"],
	params = [1,1]1
)





```