#!/usr/bin/env python3

import kfp
from kfp import components
from kfp import dsl
from kubeflow_host import KubeflowHost
from dotenv import dotenv_values

EXPERIMENT_NAME = 'Add number pipeline'
BASE_IMAGE = "python:3.7"


@dsl.python_component(
    name='add_op',
    description='adds two numbers', 
    base_image=BASE_IMAGE
)
def add(a: float, b: float) -> float:
    '''Calculates sum of two arguments'''
    print(a, '+', b, '=', a + b)
    return a + b

add_op = components.func_to_container_op(
    add,
    base_image=BASE_IMAGE,
)

@dsl.pipeline(
    name='Calculation pipeline',
    description='A toy pipeline that performs arithmetic calculations.'
)
def calc_pipeline(
        a: float = 0,
        b: float = 7
):
    add_task = add_op(a, 4)
    add_2_task = add_op(a, b)
    add_3_task = add_op(add_task.output, add_2_task.output)
    
    return add_3_task.output


if __name__ == "__main__":
    env = dotenv_values('.env')
    
    kubeflow_host = KubeflowHost(
        env.get("HOST"),
        env.get("USERNAME"),
        env.get("PASSWORD"),
        env.get("NAMESPACE")
    )
    
    session_cookie = kubeflow_host.get_session_cookie()
    kfp_client = kubeflow_host.get_kfp_client()
    
    arguments = {'a': '7', 'b': '8'}
    kfp_client.create_run_from_pipeline_func(
        calc_pipeline,
        arguments=arguments,
        experiment_name=EXPERIMENT_NAME
    )

