import kfp
import kfp.components
from kfp import dsl
from kfp.compiler import Compiler

from kubeflow_host import KubeflowHost
from dotenv import dotenv_values

@dsl.pipeline(
    name="iris_train_pipeline",
    description="train iris data"
)
def iris_pipeline(registry: str):
    load = dsl.ContainerOp(
        name="load iris data",
        image=f"{registry}/load_data:latest",
        arguments=[
            "--data_path", "/iris.csv"
        ],
        file_outputs={
            "iris": "/iris.csv"
        }
    )
    
    train = dsl.ContainerOp(
        name="train iris data",
        image=f"{registry}/train:latest",
        arguments=[
            "--data", load.outputs["iris"]
        ],
    )
    
    train.after(load)

if __name__ == "__main__":
    env = dotenv_values('.env')
    
    Compiler().compile(iris_pipeline, __file__ + '.tar.gz')
    
    kubeflow_host = KubeflowHost(
        env.get("HOST"),
        env.get("USERNAME"),
        env.get("PASSWORD"),
        env.get("NAMESPACE"),
    )

    kfp_client = kubeflow_host.get_kfp_client()

    arguments = {
        "registry": env.get("REGISTRY"),
    }
    
    kfp_client.upload_pipeline(
        pipeline_package_path="main.py.tar.gz",
        pipeline_name="iris_train_pipeline"
    )
    
    kfp_client.create_run_from_pipeline_func(
        iris_pipeline,
        arguments=arguments,
        experiment_name="iris_train_experiment"
    )
