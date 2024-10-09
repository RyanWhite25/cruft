def clean_context(context):
    cleanedContext = context
    keysToRemove = ["_output_dir", "_repo_dir"]
    for key in keysToRemove:
        if key in cleanedContext["cookiecutter"]:
            del cleanedContext["cookiecutter"][key]
    
    return cleanedContext
