wget https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv5.2.1/kustomize_v5.2.1_darwin_arm64.tar.gz
tar -xzf kustomize_v5.2.1_darwin_arm64.tar.gz
chmod +x kustomize
sudo mv kustomize /usr/local/bin/kustomize
export PATH=$PATH:/usr/local/bin/kustomize
kustomize version
