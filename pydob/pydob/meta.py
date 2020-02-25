def get_funcs_for_dataset(dataset_name, globals_dict):
    functionality = lambda f_name: f_name[len(dataset_name)+1:]

    return {
                functionality(k): v
                    for k, v in globals_dict.items()
                    if k.startswith(dataset_name)
                                
                }