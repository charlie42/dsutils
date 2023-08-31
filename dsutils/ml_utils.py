def get_base_model_name_from_estimator(estimator):
    return estimator.__class__.__name__.lower()

def get_estimator_from_pipeline(pipeline):
    return pipeline.steps[-1][1]

def get_base_model_name_from_pipeline(pipeline):
    estimator = get_estimator_from_pipeline(pipeline)
    return get_base_model_name_from_estimator(estimator)