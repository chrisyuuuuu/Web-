1. 登录成功，request.session["username"] = obj.username
2. 第二次来的时候，检测request.session.get("username")
3. 数据库，缓存，文件，缓存+数据库，加密cookie