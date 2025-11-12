# create virtual env
```
curl https://pyenv.run | bash
export PYENV_ROOT="$HOME/.pyenv" && export PATH="$PYENV_ROOT/bin:$PATH" && eval "$(pyenv init - bash)"
pyenv install 3.11.13
export PYENV_ROOT="$HOME/.pyenv" && export PATH="$PYENV_ROOT/bin:$PATH" && eval "$(pyenv init - bash)" && pyenv global 3.11.13 && python -m venv .myenv
source .myenv/bin/activate && python --version && which python
# don't upgrade poetry
pip install  poetry==1.8.3
poetry lock
```
# build gpustack ui
## install nodejs 18
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/refs/heads/master/install.sh | bash
nvm install 18

```
## build gpustack ui
```
nvm use 18
cd gpustack-ui
npm run build
rm -rf ../gpustack/uidist ; cp -ap dist ../gpustack/uidist

cd ../gpustack
ROOT_DIR=`pwd`
extra_static_path="${ROOT_DIR}/static"
ui_static_path="${ROOT_DIR}/uidist/static"
cp -a "${extra_static_path}/." "${ui_static_path}"

```
## update ui
```
cd gpustack-ui
rsync -auvP dist/ ../gpustack/uidist/
```
# build gpustack user guide
```
pip install -i https://mirrors.aliyun.com/pypi/simple mkdocs==1.6.1 mkdocs-material==9.6.11 mkdocs-print-site-plugin==2.7.3 mkdocs-glightbox==0.4.0 mkdocs-static-i18n==1.3.0
mkdocs  build  -f mkdocs-zh.yml
```
the manual is put at 'site'.

# build gpustack with multi stage
```
export DOCKER_BUILDKIT=1
export PROXY=172.16.12.59
export VERSION=v0.7.0-15
```

```
docker buildx build --build-arg https_proxy=http://$PROXY:7890 --target base -t base:latest -f Dockerfile.new .
docker buildx build --build-arg https_proxy=http://$PROXY:7890 --target base-build -t base-build:latest -f Dockerfile.new .
docker buildx build --build-arg https_proxy=http://$PROXY:7890 --target flashinfer-build -t flashinfer-build:latest -f Dockerfile.new .

docker buildx build --build-arg https_proxy=http://$PROXY:7890 --target flashinfer-install -t flashinfer-install:latest -f Dockerfile.new .

```

```
echo $VERSION > hack/lib/.version
docker buildx build --build-arg https_proxy=http://$PROXY:7890 \
  -t aimindserve:$VERSION -f Dockerfile.new \
  --platform linux/amd64 \
  --cache-from base:latest,base-build:latest,flashinfer-build:latest,flashinfer-install:latest . 2>&1 | tee log$VERSION.txt
```

```
docker tag aimindserve:$VERSION registry.aimall.ai-links.com/ailinks/aimindserve:$VERSION
docker save registry.aimall.ai-links.com/ailinks/aimindserve:$VERSION -o aimindserve-$VERSION.tar
```

# run
```
MODELSPATH=/opt/aimindserve-models/
docker stop aimindserve-server; docker rm aimindserve-server
docker run -d --name aimindserve-server \
    --restart=unless-stopped \
    --network=host \
    --ipc=host \
    -v gpustack-data:/var/lib/gpustack \
    -v ${MODELSPATH}:/data/models \
    -v /root/gpustack/gpustack/gpustack/assets/model-catalog-modelscope-zh.yaml:/etc/model-catalog.yaml \
    -v /root/gpustack/gpustack/site:/manual \
    -v /root/gpustack/gpustack/uidist:/ui \
    -e PIP_INDEX=https://mirrors.aliyun.com/pypi/simple/ \
    -e HF_ENDPOINT=https://hf-mirror.com \
    -e GPUSTACK_DEBUG=True \
    registry.aimall.ai-links.com/ailinks/aimindserve:$VERSION \
    --bootstrap-password=ailinks@1QAZ --port 32080 --debug --cache-dir /data/models --model-catalog-file /etc/model-catalog.yaml --disable-worker
```

or to run with aifare:
use the command to identify the gpus id and uuid:
```
nvidia-smi --query-gpu=index,uuid --format=csv,noheader,nounits
```
use the aifare admin to specify bypassing some gpus, for example we bypassed the 3-6 gpus. then run aimindserve with following command parameters:
```
  --gpus '"device=3,4,5,6"' \
  --label gpu.direct=3,4,5,6 \
```
Use the following command to get token to be used by worker(s):
```
docker exec -it aimindserve-server cat /var/lib/gpustack/token
```

# fix bug
```
docker exec  aimindserve-server rm -f /usr/local/lib/python3.11/dist-packages/gpustack/routes/__pycache__/proxy.cpython-311.pyc
docker cp gpustack/gpustack/routes/proxy.py aimindserve-server:/usr/local/lib/python3.11/dist-packages/gpustack/routes/proxy.py

docker exec  aimindserve-server rm -f /opt/venvs/gpustack/lib/python3.11/site-packages/gpustack/routes/__pycache__/ui.cpython-311.pyc
find /root/tmp/uidist/static/ -maxdepth 1 -name "*.png" -exec docker cp {} aimindserve:/opt/venvs/gpustack/lib/python3.11/site-packages/gpustack/ui/static/ \;
```
# worker
```
docker stop worker3; docker rm worker3
docker run -d --name worker3 --restart=unless-stopped \
--gpus all --network=host --ipc=host \
-v gpustack-worker-data:/var/lib/gpustack \
-v /gm-models:/data/models \
-e PIP_INDEX=https://mirrors.aliyun.com/pypi/simple/ \
-e HF_ENDPOINT=https://hf-mirror.com \
aimindserve:v0.7.0-12 \
--server-url https://models.dev.ai-links.com \
--token 06fa7f609642fbea3a02d7dc41a40a5a --worker-ip 10.20.10.13 --debug --cache-dir /data/models
```


# quick patch community images‘s ui and doc
```
tar -czvf aimind.tar.gz uidist site gpustack/routes/ui.py
rsync -avuP aimind.tar.gz lxgpu:~/
docker cp gpustack/routes/ui.py gpustack:/opt/venvs/gpustack/lib/python3.11/site-packages/gpustack/routes/ui.py
find uidist/static/ -maxdepth 1 -name "*.png" -exec docker cp {} aimindserve:/opt/venvs/gpustack/lib/python3.11/site-packages/gpustack/ui/static/ \;
docker restart gpustack
```