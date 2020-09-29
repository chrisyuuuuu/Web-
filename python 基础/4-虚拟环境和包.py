# pip freeze
# 将生成一个类似的已安装包列表，但输出使用 pip install 期望的格式。一个常见的约定是将此列表放在 requirements.txt 文件中
  # pip freeze > requirements.txt
  # cat requirements.txt
# 然后可以将 requirements.txt 提交给版本控制并作为应用程序的一部分提供。然后用户可以使用 install -r 安装所有必需的包
  # pip install -r requirements.txt