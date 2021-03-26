# podman容器

## portainer

```shell
docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /run/podman/podman.sock:/var/run/docker.sock -v /home/podman-share/portainer_data:/data portainer/portainer-ce
```