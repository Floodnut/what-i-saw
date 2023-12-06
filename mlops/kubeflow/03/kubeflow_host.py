import requests
import kfp

class KubeflowHost():
    def __init__(self, host, username, password, namespace):
        self.host = host
        self.kubeflow_host = f"{host}/pipeline"
        self.namespace = namespace
        
        self.data = {
            "login": username,
            "password": password,
        }
        
    def get_session_cookie(self):
        session = requests.Session()
        response = session.get(self.host)

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
                
        session.post(response.url, headers=headers, data=self.data)
        session_cookie = session.cookies.get_dict()["authservice_session"]
        
        return session_cookie
    
    def get_kfp_client(self) -> kfp.Client:
        session_cookie = self.get_session_cookie()
        
        return kfp.Client(
            host=self.kubeflow_host,
            namespace=f"{self.namespace}",
            cookies=f"authservice_session={session_cookie}",
        )