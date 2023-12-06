# 각 컴포넌트가 디렉터리를 출력하는 방법
# 파일 출력과 유사하게, 컴포넌트는 출력 경로를 받아 해당 경로에 데이터를 씀.
# 시스템은 해당 데이터를 가져와 하위 컴포넌트에서 사용할 수 있도록 함.
# 파일을 출력하려면 출력 경로에 새 파일을 생성.
# 디렉터리를 출력하려면 출력 경로에 새 디렉터리를 생성.

from kfp.components import create_component_from_func, load_component_from_text, InputPath, OutputPath
from kubeflow_host import KubeflowHost
from dotenv import dotenv_values

EXPERIMENT_NAME = 'Output a directory'  # 실험 명

@create_component_from_func
def produce_dir_with_files_python_op(output_dir_path: OutputPath(), num_files: int = 10):
    import os
    os.makedirs(output_dir_path, exist_ok=True)
    for i in range(num_files):
        file_path = os.path.join(output_dir_path, str(i) + '.txt')
        with open(file_path, 'w') as f:
            f.write(str(i))


@create_component_from_func
def list_dir_files_python_op(input_dir_path: InputPath()):
    import os
    dir_items = os.listdir(input_dir_path)
    for dir_item in dir_items:
        print(dir_item)

# CLI 환경에서 ouput 디렉토리를 생성하고 파일을 생성하는 컴포넌트를 만들고 실행
produce_dir_with_files_general_op = load_component_from_text('''
name: Produce directory
inputs:
- {name: num_files, type: Integer}
outputs:
- {name: output_dir}
implementation:
  container:
    image: alpine
    command:
    - sh
    - -ecx
    - |
      num_files="$0"
      output_path="$1"
      mkdir -p "$output_path"
      for i in $(seq "$num_files"); do
        echo "$i" > "$output_path/${i}.txt"
      done
    - {inputValue: num_files}
    - {outputPath: output_dir}
''')


list_dir_files_general_op = load_component_from_text('''
name: List dir files
inputs:
- {name: input_dir}
implementation:
  container:
    image: alpine
    command:
    - ls
    - {inputPath: input_dir}
''')

def dir_pipeline():
    produce_dir_python_task = produce_dir_with_files_python_op(num_files=15)
    list_dir_files_python_op(input_dir=produce_dir_python_task.output)

    produce_dir_general_task = produce_dir_with_files_general_op(num_files=15)
    list_dir_files_general_op(input_dir=produce_dir_general_task.output)


if __name__ == '__main__':
    env = dotenv_values('.env')
    
    kubeflow_host = KubeflowHost(
        env.get("HOST"),
        env.get("USERNAME"),
        env.get("PASSWORD"),
        env.get("NAMESPACE")
    )
    
    kfp_client = kubeflow_host.get_kfp_client()
  
    kfp_client.create_run_from_pipeline_func(
        dir_pipeline,
        arguments={},
        experiment_name=EXPERIMENT_NAME)