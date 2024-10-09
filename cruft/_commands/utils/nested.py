def is_nested_template(context):
    return bool({"template", "templates"} & set(context["cookiecutter"].keys()))
