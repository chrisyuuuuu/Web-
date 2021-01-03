### TemplateView

- 模板型的View
- 直接渲染模板
- 默认实现了get
  - get_context_data
  - render_to_response
- 父类
  - TemplateResponseMixin
    - template_name
    - template_engine
    - response_class
    - content_type
    - render_to_response
    - get_template_names
  - ContextMixin
    - get_context_data
  - View
